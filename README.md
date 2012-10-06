Gmail-exporter
==============

Python script for picking up e-mail addresses from specific letters in Gmail. We only use it as service util for our mailing list.

Search criteria examples
-----------------------
*  <code>(FROM "ex@example.com" UNSEEN)</code>
*  <code>(FROM "ex@example.com" SEEN SINCE "31-Dec-2012" BEFORE "01-Jan-2013" SUBJECT "Free beer" TEXT "Text from body")</code>

Search criteria tips
----------------------
* ALL &mdash; return all messages matching the rest of the criteria
* ANSWERED &mdash; match messages with the \\ANSWERED flag set
* BCC "string" &mdash; match messages with "string" in the Bcc: field
* BEFORE "date" &mdash; match messages with Date: before "date"
* BODY "string" &mdash; match messages with "string" in the body of the message
* CC "string" &mdash; match messages with "string" in the Cc: field
* DELETED &mdash; match deleted messages
* FLAGGED &mdash; match messages with the \\FLAGGED (sometimes referred to as Important or Urgent) flag set
* FROM "string" &mdash; match messages with "string" in the From: field
* KEYWORD "string" &mdash; match messages with "string" as a keyword
* NEW &mdash; match new messages
* OLD &mdash; match old messages
* ON "date" &mdash; match messages with Date: matching "date"
* RECENT &mdash; match messages with the \\RECENT flag set
* SEEN &mdash; match messages that have been read (the \\SEEN flag is set)
* SINCE "date" &mdash; match messages with Date: after "date"
* SUBJECT "string" &mdash; match messages with "string" in the Subject:
* TEXT "string" &mdash; match messages with text "string"
* TO "string" &mdash; match messages with "string" in the To:
* UNANSWERED &mdash; match messages that have not been answered
* UNDELETED &mdash; match messages that are not deleted
* UNFLAGGED &mdash; match messages that are not flagged
* UNKEYWORD "string" &mdash; match messages that do not have the keyword "string"
* UNSEEN &mdash; match messages which have not been read yet

or PHP imap_search <a href="http://php.net/manual/ru/function.imap-search.php">manual</a>