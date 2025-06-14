import stanza

nlp = stanza.Pipeline('en')

text = "Deep in the heart of the jungle, where the trees whispered secrets and the rivers sang old songs, a young monkey named Tiko swung from vine to vine. Unlike the others in his troop, Tiko was always curious about the unknown.One day, he noticed an old parrot named Azul perched on a twisted tree, watching him closely.Why do you always explore alone, little one? Azul croaked.I'm looking for something special, Tiko replied. Something no one has ever seen before.Azul fluffed his feathers. Then you should visit the Hidden Falls. But beware—the jungle only shares its secrets with those who listen.Excited, Tiko followed Azul’s directions, navigating thick vines and stepping over glowing mushrooms until he heard the distant roar of water. As he reached the falls, he saw something incredible—a shimmering pool reflecting the entire jungle, but in reverse. The sky was green, the leaves were blue, and in the reflection, Tiko saw animals he had never met before.Suddenly, a jaguar’s reflection moved—yet there was no jaguar behind him. The jungle wasn’t just showing him another world; it was revealing what the eye couldn t see. Tiko realized that knowledge wasn’t just about seeing—it was about understanding.When he returned to his troop, he no longer searched for something special.  Instead, he shared the wisdom of the jungle, teaching others to listen, observe, and appreciate the mysteries hidden in plain sight.And so, the jungle whispered a new secret—that the greatest discoveries come to those who seek not just with their eyes, but with their hearts."

doc = nlp(text)

entities = []
relationships = []

for ent in doc.ents:
    entities.append((ent.text, ent.type))

for sent in doc.sentences:
    subject = None
    verb = None
    obj = None

    for word in sent.words:
        if 'nsubj' in word.deprel:
            subject = word.text
        elif word.upos == 'VERB':
            verb = word.text
        elif word.deprel in ['obj', 'iobj', 'obl']:
            obj = word.text

        if subject and verb and obj:
            relationships.append((subject, verb, obj))
            obj = None

    subject = None
    verb = None

print('Entities:', entities)
print('Relationships:', relationships)
