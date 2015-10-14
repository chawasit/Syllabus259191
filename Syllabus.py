#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# Syllabus259191 - http://github.com/chawasit/Syllabus259191
# Copyright 2015 Chawasit Tengtrairatana <chawasit_teng@cmu.ac.th>

from __future__ import print_function
import requests, gevent, time, getpass
from bs4 import BeautifulSoup


class Syllabus():
    def __init__(self, username, password, pole_id, choice):
        # Input
        self.username = username
        self.password = password
        self.pole_id = pole_id
        self.choice = choice
        #flag
        self.voted = False
        self._voted = False
        # HTTP Session
        self.session = requests.Session()
        self.logined = self._login()
        
        if not self.logined:
            raise ValueError
        else:
            self.sesskey, self.choice_id, self.voted = self._get_data()

    def _get_data(self):
        url = "https://elearning.cmu.ac.th/mod/choice/view.php?id=%s" % (self.pole_id, )
        response = self.session.get(url)
        soup = BeautifulSoup( response.text, "html5lib")
        sesskey = soup.find("input", attrs={'name':"sesskey"}).get('value')
        choice_id = soup.find("input", attrs={'name':"answer", 'id':"choice_%s"%(self.choice)}).get('value')
        voted = ("Remove my choice" in response.text)
        return sesskey, choice_id, voted

    def _login(self):
        url = "https://elearning.cmu.ac.th/login/index.php"
        data = {"username": self.username, "password": self.password}
        response = self.session.post(url, data=data)
        return ("Logged in user" in response.text)

    def _vote(self, pid):
        while not self._voted:
            print("[t%d] Sent vote"%(pid), time.ctime())
            url = "https://elearning.cmu.ac.th/mod/choice/view.php"
            data = {"answer": self.choice_id, "sesskey": self.sesskey, "id": self.pole_id }
            response = self.session.post(url, data=data)
            soup = BeautifulSoup( response.text, "html5lib")
            checked = soup.find("input", attrs={'name':"answer", 'id':"choice_%s"%(self.choice), 'checked':"1"})
            if checked is not None:
                self._voted = True

    def vote(self):
        self._voted = False
        from gevent.pool import Pool
        p = Pool(10)
        p.map(self._vote, xrange(0,5))
        p.join()
        if self._voted:
            self.vote = True
            print("[+] Vote Success", time.ctime())
        else:
            print("[!] Something Wrong", time.ctime())

    def unvote(self):
        url = "https://elearning.cmu.ac.th/mod/choice/view.php?id=%s&action=delchoice&sesskey=%s" % (self.pole_id, self.sesskey)
        response = self.session.get(url)
        if ("Remove my choice" not in response.text):
            self.voted = False
            print("[+] Unvote Success", time.ctime())

    def status(self):
        print("[!] Voted:", self.voted)
        return self.voted

    def set_choice(self, choice):
        self.choice = choice
        self.sesskey, self.choice_id, self.voted = self._get_data()
        print("[+] Set choice:", choice)


def get_choice():
    return (raw_input("Choice (default 1): ") or 1)

def init():
    while True:
        username = raw_input("Username (xxx@cmu.ac.th): ")
        password = getpass.getpass("Password:")
        pole_id = raw_input("Pole id: ")
        choice = get_choice()
        try:
            s = Syllabus(username, password, pole_id, choice)
        except:
            print("ERROR! Please check your input.")
        else:
            break
    return s

if __name__ == "__main__":
    print("##########################")
    print("#       Syllabus        #")
    print("##########################")
    s = init()
    try:
        command = [s.vote, s.unvote, s.status]
        while True:
            print("Command:  1 vote")
            print("          2 unvote")
            print("          3 status")
            print("          4 set choice")
            c = raw_input("Select : ") or 3
            if c=="4":
                s.set_choice(get_choice())
            else:
                command[int(c)-1]()


    except KeyboardInterrupt:
        pass