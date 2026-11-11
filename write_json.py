import json

data = {
  "novel": "Override Zone: The 'Hart' that shall beat",
  "characters": [
    {
      "name": "Niro Hart",
      "aliases": ["the thirteenth", "the mistake", "devil in white", "prodigy"],
      "role": "Protagonist of the origin story; future antagonist/rival; Malevolence Mana user and ruler of Hart Industries",
      "bio": "Born the thirteenth child of the cruel Hart family, Niro is abused from age eight as the 'mistake.' He awakens Malevolence Mana at his grandfather's funeral and is forged by years of 'lessons' from his siblings and father's contempt. After his only ally Thad is murdered by his siblings, he slaughters nearly the entire family at sixteen, inherits the empire, and builds Hart Industries into a quintillionaire powerhouse. At twenty-seven, bored, he turns toward rumors of a boy in Tokyo bonded to an ancient maiden.",
      "first_appearance_context": "Standing at the back of the family line at Grandfather Elias Hart's funeral, eight years old, hands shaking and already sparking red Malevolence Mana."
    },
    {
      "name": "Victor Hart",
      "aliases": ["Father", "head of the Hart family"],
      "role": "Antagonist; patriarch of the Hart family; CEO of Hart Industries",
      "bio": "Tall, imposing patriarch who rules his family like a kingdom. He teaches that weakness is a disease, oversees Niro's brutal 'lessons,' and dismisses Thad's pleas. He is killed by Niro during the massacre when a wave of Malevolence Mana crushes his ribs against the wall.",
      "first_appearance_context": "Stepping to the podium at Elias Hart's funeral to deliver the speech about strength and weakness."
    },
    {
      "name": "Elena Hart",
      "aliases": ["Mother", "Elena"],
      "role": "Antagonist by inaction; matriarch who chooses survival over protecting Niro",
      "bio": "Niro's silent mother, elegant and empty-eyed. She watches the abuse from behind one-way glass but never intervenes, believing acknowledgment would paint targets on both of them. She survives the massacre and is forced to lie to police that it was a home invasion. Her punishment is to live knowing what she helped create.",
      "first_appearance_context": "Standing beside Victor at the funeral, elegant and silent, never looking at her youngest son."
    },
    {
      "name": "Elias Hart",
      "aliases": ["Grandfather Elias"],
      "role": "Deceased founder of the Hart empire",
      "bio": "Ruthless founder who built Hart Industries from nothing and whose funeral sets the story in motion. His 'weakness is a disease' philosophy, delivered at his funeral, becomes the curse that shapes Niro.",
      "first_appearance_context": "Being buried at the Hart family cemetery as Victor eulogizes him."
    },
    {
      "name": "Thaddeus Hart",
      "aliases": ["Thad", "Thaddy"],
      "role": "Ally; Niro's only kind brother",
      "bio": "Seventeen when introduced, the only sibling who treats Niro like a person. He tries to shield Niro, pleads with Victor to stop the lessons, and promises to get him out. His siblings murder him on the mountain road to remove his influence. His death snaps the last thread of Niro's mercy.",
      "first_appearance_context": "Sliding into the seat next to eight-year-old Niro in the funeral limousine, whispering comfort."
    },
    {
      "name": "Seraphine Hart",
      "aliases": ["Sera", "the golden child", "designated heir"],
      "role": "Antagonist; eldest sister and designated heir",
      "bio": "The cruelest sibling, who makes Niro recite his worthlessness and grooms herself as CEO. She conspires with Edward and Nigel to kill Thad, then is herself killed when Niro's compressed Malevolence orb detonates her during the massacre, leaving a smoking crater.",
      "first_appearance_context": "Whispering 'Look at the little mistake shaking. Pathetic.' at the funeral."
    },
    {
      "name": "Edward Hart",
      "aliases": [],
      "role": "Antagonist; sadistic brother",
      "bio": "A brother who runs psychological 'lessons,' locking young Niro in dark rooms. He confesses to helping murder Thad. He is the first killed in the massacre, stumbling into the dining hall with a shotgun wound to the head.",
      "first_appearance_context": "Locking Niro in a dark storage room with a single candle as a 'lesson.'"
    },
    {
      "name": "Nigel Hart",
      "aliases": [],
      "role": "Antagonist; brutal brother",
      "bio": "The physical enforcer of the lessons, making Niro run until collapse. He joins the conspiracy to kill Thad and is killed during the massacre when a compressed Malevolence orb blows a hole through his chest.",
      "first_appearance_context": "Making young Niro run laps and dragging him up by the collar."
    },
    {
      "name": "Mireille Vale",
      "aliases": ["Master's blade", "yandere secretary"],
      "role": "Antagonist/ally; Niro's devoted secretary and enforcer",
      "bio": "A brilliant corporate-law graduate who has watched Niro for two years and joins him out of obsessive devotion. She kills for him without hesitation, breaks Director Cho's wrist, and manages his empire with terrifying efficiency. She worships him as her god.",
      "first_appearance_context": "Stepping into the empty boardroom at age twenty-one to interview for the executive assistant position."
    },
    {
      "name": "Lucien Moreau",
      "aliases": ["Weaver of Time"],
      "role": "Mentor; one of the 12 True Weavers",
      "bio": "The Weaver of Time who trains fourteen-year-old Niro in the Override Zone after the boy accidentally tears into it. He teaches Niro to compress his Malevolence Mana and warns that consequences always find their way back. He watches possible futures without interfering.",
      "first_appearance_context": "Standing on the obsidian island in the Override Zone as Niro is spat out of a torn hole in reality."
    },
    {
      "name": "Director Cho",
      "aliases": [],
      "role": "Antagonist; board director of Hart Industries",
      "bio": "A sixty-year-old director loyal to Victor Hart who moves for a no-confidence vote against Niro. Niro exposes his crimes, and Mireille breaks his wrist and threatens him with a Malevolence needle until he retires, securing Niro's control.",
      "first_appearance_context": "Slamming his folder on the 47th-floor boardroom table during a rainstorm."
    }
  ],
  "factions": [
    {
      "name": "Hart family",
      "desc": "A wealthy, ruthless bloodline that measures love in obedience and treats weakness as a disease. Its members abuse the thirteenth child, Niro, until he destroys them."
    },
    {
      "name": "Hart Industries",
      "desc": "The global powerhouse founded by Elias Hart and seized by Niro at sixteen. It develops mana-infused technology, including the Malevolence engine and mobility divisions."
    },
    {
      "name": "The 12 True Weavers",
      "desc": "An order of powerful mana Weavers. Lucien Moreau, Weaver of Time, belongs to it and trains Niro in the Override Zone."
    },
    {
      "name": "Ivory Board",
      "desc": "An external body whose shell corporation buys stolen Hart Industries engine schematics, mentioned as part of Director Cho's treachery."
    }
  ],
  "locations": [
    {
      "name": "Hart family cemetery",
      "desc": "Where Elias Hart is buried and eight-year-old Niro first sparks Malevolence Mana."
    },
    {
      "name": "Hart manor",
      "desc": "The family estate containing the training hall, portrait room, dining hall, west study, Thad's shrine-room, Niro's small room, and Victor's study."
    },
    {
      "name": "Training hall beneath the manor",
      "desc": "A cold marble chamber lined with mirrors where Niro's 'lessons' are administered."
    },
    {
      "name": "Override Zone",
      "desc": "A dimension outside of time made of violet-black void and floating obsidian islands, where Lucien trains Niro to compress Malevolence Mana."
    },
    {
      "name": "Hart Industries headquarters (47th floor)",
      "desc": "The boardroom where Niro confronts and breaks Director Cho."
    },
    {
      "name": "Mountain road",
      "desc": "Where Thaddeus Hart is murdered in a staged car accident."
    },
    {
      "name": "Hospital",
      "desc": "Where Elena Hart is interviewed by detectives and repeats the home-invasion lie."
    }
  ],
  "concepts": [
    {
      "term": "Malevolence Mana",
      "desc": "Raw red mana of will to dominate, wielded by Niro. It can be projected as waves, compressed into explosive orbs or needles, and used to crush, blast, or kill."
    },
    {
      "term": "Override Zone",
      "desc": "A dimension outside of time that responds to those with enough will to break into it; used as a training ground where consequences still return."
    },
    {
      "term": "Seams",
      "desc": "A unit for measuring mana output; Niro hears of a Tokyo boy leaking Corruption Mana in the tens of thousands of Seams."
    },
    {
      "term": "Weakness is a disease",
      "desc": "The Hart family creed, spoken by Victor and Elias, that justifies abuse and becomes Niro's justification for slaughter."
    },
    {
      "term": "Home invasion cover story",
      "desc": "The lie Elena is forced to tell police, blaming masked intruders for the massacre."
    },
    {
      "term": "Mana-infused technology",
      "desc": "Hart Industries' development of products powered by controlled mana, including autonomous vehicles and Malevolence engines."
    }
  ],
  "events": [
    {
      "title": "Funeral of Elias Hart",
      "summary": "At eight years old, Niro attends his grandfather's funeral, hears Victor's creed that weakness is a disease, and ignites the first spark of Malevolence Mana.",
      "participants": ["Niro Hart", "Victor Hart", "Elena Hart", "Thaddeus Hart", "Seraphine Hart", "Edward Hart", "Nigel Hart"]
    },
    {
      "title": "The Lessons (ages 8-12)",
      "summary": "Victor and four siblings subject Niro to physical, psychological, and verbal abuse in the training hall, forging his hatred and resolve.",
      "participants": ["Niro Hart", "Victor Hart", "Thaddeus Hart", "Edward Hart", "Nigel Hart", "Seraphine Hart", "Elena Hart"]
    },
    {
      "title": "Mother's Choice",
      "summary": "Elena watches Niro's abuse from behind one-way glass and chooses silence and survival over protecting him.",
      "participants": ["Elena Hart", "Niro Hart", "Seraphine Hart", "Victor Hart"]
    },
    {
      "title": "Accidental Entry into the Override Zone",
      "summary": "Fourteen-year-old Niro, beaten and angry, tears a hole into the Override Zone and meets Lucien Moreau, who allows him to train there.",
      "participants": ["Niro Hart", "Lucien Moreau"]
    },
    {
      "title": "Override Zone Training: How to Hold Hate",
      "summary": "Lucien teaches Niro to compress his screaming Malevolence Mana into dense, controlled orbs, marking his first real step toward power.",
      "participants": ["Niro Hart", "Lucien Moreau"]
    },
    {
      "title": "Thad's Plea to Victor",
      "summary": "Thad asks Victor to stop Niro's lessons and offers to surrender his inheritance; Victor refuses and Seraphine mocks him.",
      "participants": ["Thaddeus Hart", "Victor Hart", "Seraphine Hart"]
    },
    {
      "title": "Murder of Thaddeus Hart",
      "summary": "Seraphine, Edward, and Nigel stage Thad's death as a car accident on the mountain road to remove his protection of Niro.",
      "participants": ["Thaddeus Hart", "Seraphine Hart", "Edward Hart", "Nigel Hart", "Niro Hart"]
    },
    {
      "title": "Discovery of the Murder Plot",
      "summary": "On the eve of his sixteenth birthday, Niro overhears Seraphine, Edward, and Nigel confessing that they killed Thad, snapping his last mercy.",
      "participants": ["Niro Hart", "Seraphine Hart", "Edward Hart", "Nigel Hart"]
    },
    {
      "title": "Hart Family Massacre",
      "summary": "Sixteen-year-old Niro slaughters his father and ten siblings with Malevolence Mana during a family dinner, sparing only his mother.",
      "participants": ["Niro Hart", "Victor Hart", "Seraphine Hart", "Edward Hart", "Nigel Hart", "Elena Hart"]
    },
    {
      "title": "The Quiet After Blood",
      "summary": "After the massacre, Niro visits Thad's shrine-room, changes into a clean identical outfit, and steels himself before seizing the empire.",
      "participants": ["Niro Hart"]
    },
    {
      "title": "Cover-Up and Inheritance",
      "summary": "Niro coerces Elena into telling police a home-invasion story, transfers ownership of Hart Industries, and inherits everything at sixteen.",
      "participants": ["Niro Hart", "Elena Hart"]
    },
    {
      "title": "Police Interview",
      "summary": "Elena repeats the home-invasion lie to detectives while Niro watches through the glass with his demonic smile.",
      "participants": ["Elena Hart", "Niro Hart"]
    },
    {
      "title": "Hiring of Mireille Vale",
      "summary": "At nineteen, Niro hires Mireille as his secretary after she declares her obsessive devotion to his ego and elegance.",
      "participants": ["Niro Hart", "Mireille Vale"]
    },
    {
      "title": "First Boardroom Kill",
      "summary": "Niro exposes Director Cho's crimes and has Mireille break his wrist and threaten him, forcing Cho's retirement and securing the board.",
      "participants": ["Niro Hart", "Mireille Vale", "Director Cho"]
    },
    {
      "title": "Empire Building and Boredom",
      "summary": "From nineteen to twenty-seven, Niro expands Hart Industries, kills when necessary, and grows bored as a quintillionaire.",
      "participants": ["Niro Hart", "Mireille Vale"]
    },
    {
      "title": "Rumor of the Tokyo Vessel",
      "summary": "At twenty-seven, Niro hears of a boy in Tokyo bonded to an ancient maiden and leaking Corruption Mana, sparking his interest.",
      "participants": ["Niro Hart"]
    }
  ],
  "quotes": [
    {
      "speaker": "Victor Hart",
      "quote": "My father taught us one thing above all else: weakness is a disease. The Hart name does not tolerate it. We cut it out. We burn it away. Strength is the only currency that matters in this world."
    },
    {
      "speaker": "Niro Hart",
      "quote": "If weakness is a disease... then I will become the cure. I will cut every single one of you out. One day."
    },
    {
      "speaker": "Seraphine Hart",
      "quote": "Say it, little brother. 'I am the thirteenth mistake. I will never inherit. I exist only because Mother failed to prevent me.'"
    },
    {
      "speaker": "Thaddeus Hart",
      "quote": "You're not alone, okay? I've got your back. We'll get through this family together."
    },
    {
      "speaker": "Niro Hart",
      "quote": "Don't promise things this family won't let you keep."
    },
    {
      "speaker": "Elena Hart",
      "quote": "Forgive me. I thought if I didn't look, they'd forget you. I didn't know they'd try to erase you."
    },
    {
      "speaker": "Niro Hart",
      "quote": "Good. Then it's mine now."
    },
    {
      "speaker": "Niro Hart",
      "quote": "I was thinking about how I'm going to kill every single one of them. Slowly."
    },
    {
      "speaker": "Lucien Moreau",
      "quote": "Time may not move here, but consequences always find their way back."
    },
    {
      "speaker": "Lucien Moreau",
      "quote": "Hate is heavy - make it dense."
    },
    {
      "speaker": "Niro Hart",
      "quote": "Did you see that? Three seconds."
    },
    {
      "speaker": "Niro Hart",
      "quote": "You watched, Mother. Every lesson. Every bruise. Every time they called me the mistake. You never said a word. So I'll let you live with it."
    },
    {
      "speaker": "Niro Hart",
      "quote": "You always said weakness is a disease, Father. I finally agree. I'm curing it tonight."
    },
    {
      "speaker": "Niro Hart",
      "quote": "Weakness is a disease. I cut it out."
    },
    {
      "speaker": "Niro Hart",
      "quote": "Live with it, Mother. That's my punishment."
    },
    {
      "speaker": "Mireille Vale",
      "quote": "I like your personality, Mr. Hart. Your unmatched ego. Your cold elegance. The way you look at people like they're already dead and just don't know it."
    },
    {
      "speaker": "Mireille Vale",
      "quote": "Only for you."
    },
    {
      "speaker": "Niro Hart",
      "quote": "You're insane."
    },
    {
      "speaker": "Mireille Vale",
      "quote": "Mr. Hart doesn't like no-confidence votes during rain. He finds them... noisy."
    },
    {
      "speaker": "Niro Hart",
      "quote": "Finally... something interesting."
    }
  ],
  "relationships": [
    {
      "pair": "Niro Hart & Victor Hart",
      "note": "Abusive father and thirteenth son; Victor's creed and lessons forge Niro's hatred, and Niro kills him during the massacre."
    },
    {
      "pair": "Niro Hart & Elena Hart",
      "note": "Mother and son bound by her silence; she watches his abuse and survives the massacre, forced to live with the truth."
    },
    {
      "pair": "Niro Hart & Thaddeus Hart",
      "note": "The only genuine bond Niro has; Thad protects him and is murdered by the other siblings, becoming the catalyst for Niro's slaughter."
    },
    {
      "pair": "Niro Hart & Seraphine Hart",
      "note": "Rival siblings; Seraphine is the golden heir who torments Niro and conspires to kill Thad, and Niro obliterates her in the massacre."
    },
    {
      "pair": "Niro Hart & Edward Hart",
      "note": "Tormentor and victim; Edward's psychological cruelty ends when Niro kills him first in the dining hall."
    },
    {
      "pair": "Niro Hart & Nigel Hart",
      "note": "Brute and target; Nigel's beatings are repaid when a Malevolence orb blows through his chest."
    },
    {
      "pair": "Niro Hart & Mireille Vale",
      "note": "Master and yandere devotee; she kills and manages for him out of obsessive worship, becoming his shadow."
    },
    {
      "pair": "Niro Hart & Lucien Moreau",
      "note": "Student and Weaver mentor; Lucien trains Niro in the Override Zone and warns that consequences return."
    },
    {
      "pair": "Thaddeus Hart & Seraphine Hart",
      "note": "Opposing siblings; Thad tries to protect Niro while Seraphine mocks him and removes him as a threat."
    },
    {
      "pair": "Victor Hart & Elena Hart",
      "note": "Patriarch and silent wife; Victor demands obedience and Elena survives by never looking at Niro."
    },
    {
      "pair": "Niro Hart & Director Cho",
      "note": "New CEO and resistant director; Niro breaks Cho's will and forces his retirement."
    }
  ]
}

with open(r"D:\develop\override-codex\extract_2.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("written")
# validate
with open(r"D:\develop\override-codex\extract_2.json", encoding="utf-8") as f:
    d = json.load(f)
print("valid", {k: (len(v) if isinstance(v,list) else v) for k,v in d.items()})
