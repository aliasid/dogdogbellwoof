# dogdogbellwoof

Notes
======

- Hangups installation:
  - git clone https://github.com/tdryer/hangups.git
  - cd hangups
  - sudo apt install python3-pip
  - (sudo?) pip3 install setuptools
  - sudo python3 setup.py install

- Manual login:
  - https://github.com/tdryer/hangups/issues/350#issuecomment-323553771

- Example test
  - python3 lookup_entities.py  --entity-identifier BBB.CCC01@gmail.com
  - python3 create_group_conversation.py --gaia-ids 102017382879890347811 --conversation-name test2
  - python3 send_message.py --conversation-id UgwXNPpciqrVqPQrqfp4AaABAQ --message-text 'Please tell me if you get this. Thanks!'
