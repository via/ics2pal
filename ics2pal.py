#!/usr/bin/env python

import email.parser
import sys
import vobject
import datetime


if __name__ == "__main__":


  #read rfc822 message from stdin
  parser = email.parser.Parser()
  msg = parser.parse(sys.stdin)


  if not msg.is_multipart():
    print "Not a multipart MIME message!"

  for part in msg.get_payload():
    if part.get_content_type() == "application/ics":
      event = part.get_payload(decode=True)
      cal = vobject.readOne(event)

      summary = cal.vevent.summary.valueRepr()
      stdate = cal.vevent.dtstart.value
      organizer = cal.vevent.organizer.valueRepr()
      if organizer.startswith("MAILTO:"):
        organizer = organizer[7:]

      paltime = stdate.strftime("%Y%m%d")

      palline = "%s    %s (from %s)" % (paltime, summary, organizer)

      print palline

