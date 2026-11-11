import json

data = {
  "novel": "Override Zone: The Blood Tournament",
  "characters": [
    {
      "name": "Naobito Yagami",
      "aliases": ["little lamb", "destined vessel", "Key of Duality", "little tinkerer", "Class-S Reality Anomaly"],
      "role": "Protagonist; Key of Duality; destined vessel of the Dark Maiden",
      "bio": "Two years after the first arc, Naobito returns as a polished, god-tier Symbiote-Host. He crashes into the Crimson Veil Arena as a violet meteor, dismantles Lord Varak, survives Isolde Aster, and awakens Sylvara Kane as the Key of Echoes. In the Hollow Shell he learns to house and rewrite Yurei's foundational code, and with Kenshi's help forces a draw against True Weaver Asha Nkosi, destroying the arena. By the end he is designated a Class-S Reality Anomaly and hides in Neo-Haven with Kenshi and Yurei.",
      "first_appearance_context": "Descending from deep space as a blazing violet meteor that shatters the Crimson Veil Arena's indestructible floor."
    },
    {
      "name": "Yurei Himura",
      "aliases": ["The Dark Maiden", "Yami no Otome", "Maiden of the Hollow Loom"],
      "role": "Antagonist/ally; ancient fallen maiden; co-pilot of the Hollow Shell",
      "bio": "Now a true partner rather than possessor, Yurei rides Naobito's mind and fights through the Hollow Shell. She guides Sylvara's Echo awakening, bridges Naobito's broken soul-nodes, and is stunned when Naobito rewrites her foundational information mid-battle to phase through Asha's Apex Mantle. She begins to accept that he can alter even her code.",
      "first_appearance_context": "Purring in Naobito's mind as they watch the Blood Tournament broadcast from deep space."
    },
    {
      "name": "Reno",
      "aliases": ["Elara's pawn", "attack dog"],
      "role": "Weaver's pawn; spatial folder; collector of leaking vessels",
      "bio": "Now 20 and sharper, Reno stands guard behind Elara in the VIP box and later fights in the Symbiote-Host bracket, killing a demon symbiote and its host in under twenty seconds with obsidian Neutralization rounds. He warns Naobito that the Weavers see him as a glitch to be patched.",
      "first_appearance_context": "Standing behind Elara in the Weavers' VIP box as Naobito arrives."
    },
    {
      "name": "Lady Elara Vane",
      "aliases": ["Weaver of Threads", "Weaver of the Third Seam"],
      "role": "One of the 12 True Weavers; tailor of vessels",
      "bio": "Watches the tournament with dark fascination, recognizing Naobito as a perfect, fully symbiotic vessel. She silences Reno's analysis with a thin smile and is stunned when Naobito and Sylvara create a fused Range Crest. She is the first to note Kenshi's unauthorized entry with an amused smirk.",
      "first_appearance_context": "Crossing her legs elegantly in the Weavers' VIP arc of thrones."
    },
    {
      "name": "Lucien Moreau",
      "aliases": ["Weaver of Time"],
      "role": "One of the 12 True Weavers; Naobito's closest ally among them",
      "bio": "The Weaver of Time shows unprecedented warmth toward Naobito, materializing a throne for him beside his own and calling him 'little tinkerer.' He reveals the existence of the Keys, the second Key (Sylvara), and warns that in some timelines Naobito is killed by the other Keys. He ends the arc moving chess pieces onto a Neo-Haven square.",
      "first_appearance_context": "Watching the broadcast with calm amusement in the VIP box."
    },
    {
      "name": "Saya Kurogane",
      "aliases": ["silver dove", "little silver dove"],
      "role": "Rank 5 Specialist; Neutralization Mage; empathetic ally",
      "bio": "Sits beside Master Kael in the VIP box, silver mana flickering nervously. She rushes to Naobito after his fight, offering a towel and reminding him he is allowed to be human. She later tends Sylvara and scolds Naobito for nearly dying while being relieved he survived.",
      "first_appearance_context": "Sitting beside her master in the Weavers' VIP box, silver mana flickering nervously."
    },
    {
      "name": "Master Kael Voss",
      "aliases": ["Weaver of Neutrality"],
      "role": "One of the 12 True Weavers; Saya's master",
      "bio": "Stoic and grave throughout, he notes Naobito's impossible mana density and later rages when Kenshi breaches security. He concludes the boy's power output exceeded containment thresholds after the arena's destruction.",
      "first_appearance_context": "Remaining stoic in the Weavers' VIP box."
    },
    {
      "name": "Niro Hart",
      "aliases": ["devil in white", "prodigy"],
      "role": "Antagonist/rival; Malevolence Mana user; Hart Industries ruler",
      "bio": "Now 29, Niro watches from his private luxury box with Mireille, calling Naobito 'little puzzle' and growing sharper in interest. He is one of the few who does not flee when the arena barrier shatters, and leaves with a quiet 'The show's over.'",
      "first_appearance_context": "Lounging in his blood-red throne in his private luxury box, wine in hand."
    },
    {
      "name": "Mireille Vale",
      "aliases": ["devoted blade"],
      "role": "Niro Hart's personal secretary; yandere devotee",
      "bio": "Kneels beside Niro with obsessive adoration, offering to eliminate anyone who looks at him too long. She watches the destruction without flinching and follows Niro away from the rubble with disdain.",
      "first_appearance_context": "Kneeling beside Niro in the private luxury box."
    },
    {
      "name": "High Weaver Selene Arkwright",
      "aliases": ["Weaver of Fate"],
      "role": "Leader of the 12 True Weavers; Weaver of Fate",
      "bio": "Bows to Hana Yagami on her arrival and later declares the Asha match a draw, designating Naobito a Class-S Reality Anomaly and sealing the footage. She watches the chaos with restrained calculation.",
      "first_appearance_context": "Frowning at the holographic participant list in the VIP box."
    },
    {
      "name": "Viktor Drago",
      "aliases": ["Weaver of Chains"],
      "role": "One of the 12 True Weavers; Weaver of Chains",
      "bio": "Hostile as ever, he demands Naobito be sealed, then later rages at Kenshi's unauthorized entry and the barrier's destruction. In the epilogue he forges a chain to bind reality itself from cosmic ore.",
      "first_appearance_context": "Seated in the Weavers' VIP box, chains rattling."
    },
    {
      "name": "Amara Khalil",
      "aliases": ["Weaver of Souls"],
      "role": "One of the 12 True Weavers; Weaver of Souls",
      "bio": "Senses Naobito's flawless symbiotic soul and later recognizes Kenshi warmly, recalling how he helped her extract a vessel without bloodshed in Neo-Haven. She is the most sympathetic Weaver.",
      "first_appearance_context": "In the Weavers' VIP box, sensing great pain and healing potential."
    },
    {
      "name": "Mei Ling Zhao",
      "aliases": ["Weaver of Silence"],
      "role": "One of the 12 True Weavers; Weaver of Silence",
      "bio": "Rarely speaks; offers only unreadable reactions. She opens her eyes in surprise at Lucien's warmth toward Naobito and at Kenshi's entrance.",
      "first_appearance_context": "Seated in the VIP box with eyes closed."
    },
    {
      "name": "Isabella Cortez",
      "aliases": ["Weaver of Flames"],
      "role": "One of the 12 True Weavers; Weaver of Flames",
      "bio": "Finds Naobito exciting and laughs at the chaos. She enjoys Kenshi's entrance and the destruction, flames dancing across her fingers.",
      "first_appearance_context": "Grinning in the VIP box with flames between her fingers."
    },
    {
      "name": "Omar al-Sayed",
      "aliases": ["Weaver of Sands"],
      "role": "One of the 12 True Weavers; Weaver of Sands",
      "bio": "Calm but wary, comparing Naobito to a great storm. He asks Amara about Kenshi when the boy appears.",
      "first_appearance_context": "Inclining his head respectfully in the VIP box."
    },
    {
      "name": "Asha Nkosi",
      "aliases": ["Weaver of Beasts"],
      "role": "One of the 12 True Weavers; Weaver of Beasts; fighter",
      "bio": "Personally insists on fighting Naobito, invoking her authority to turn the match into a 2v1 against both Naobito/Yurei and Kenshi. She unleashes Wild Hunt: Apex Mantle and survives the arena's destruction, then acknowledges both as worthy, keeping her scars as trophies in the Primal Expanse.",
      "first_appearance_context": "Grinning wildly in the VIP box, eager for violence."
    },
    {
      "name": "Dr. Elias Thorn",
      "aliases": ["Weaver of Flesh"],
      "role": "One of the 12 True Weavers; Weaver of Flesh",
      "bio": "Studies Naobito's symbiotic biology with clinical hunger and later salvages violet-black ash from the crater to draft blueprints for an artificial chimera.",
      "first_appearance_context": "Studying Naobito like a dissection in the VIP box."
    },
    {
      "name": "Freya Haldorsdottir",
      "aliases": ["Weaver of Storms"],
      "role": "One of the 12 True Weavers; Weaver of Storms",
      "bio": "Lightning crackles in her eyes as she watches; she notes the storm's approach and the possible renewal or ruin it brings.",
      "first_appearance_context": "Eyes crackling with lightning in the VIP box."
    },
    {
      "name": "Soren Blackwood",
      "aliases": ["Weaver of Shadows"],
      "role": "One of the 12 True Weavers; Weaver of Shadows",
      "bio": "Notes the shadows whisper Naobito's name and hunger for what he carries. He dryly observes that the rules are unraveling.",
      "first_appearance_context": "Darkness shifting around him in the VIP box."
    },
    {
      "name": "Hana Yagami",
      "aliases": ["Mistress of Threads", "the one who stitched the original Containment", "Ka-san"],
      "role": "Supreme being; Naobito's mother; creator of the Law of Containment",
      "bio": "Arrives at the arena in a flood of cyan mana, revealing herself as Naobito's mother and triggering a memory of his infancy as the first Key. She places him straight into the finals, drops him into the Weavers' box, and tests him by awakening Sylvara. She watches with proud, terrifying maternal satisfaction.",
      "first_appearance_context": "Stepping into the fighting pit in a perfect circle of cyan mana, instantly freezing the arena."
    },
    {
      "name": "Kiritaka Yagami",
      "aliases": [],
      "role": "Naobito's father; Hana's husband; immortal",
      "bio": "Naobito's smug, handsome, immortal father steps out of a golden Fold in deep space. He confirms he knew about the Key design, expresses pride, warns that the remaining Keys are waking, and teases Yurei before vanishing.",
      "first_appearance_context": "Stepping out of a soft golden Fold in the deep-space void, hands in his coat pockets."
    },
    {
      "name": "Lirael Thornvine",
      "aliases": [],
      "role": "Verdant Conclave Nature Mana fighter; rising star",
      "bio": "A lean, vine-haired Rank 3 Nature user who defeats Gorzak the Flayer in under thirty seconds with a single clean leaf-blade slash. She wins multiple bouts with surgical efficiency, catching Naobito's attention as a quiet, deadly lower-rank fighter.",
      "first_appearance_context": "Stepping into the pit as the first official match fighter."
    },
    {
      "name": "Lord Varak of the Red Abyss",
      "aliases": [],
      "role": "Abyssal Dominion demon lord; challenger",
      "bio": "A towering, red-skinned demon lord who shatters Hana's incomplete gate to fight Naobito himself. He charges with raw Malevolence Mana but is systematically dismantled and bound in violet bandages within seconds.",
      "first_appearance_context": "Exploding through the incomplete Folded gate, roaring at the Mistress."
    },
    {
      "name": "Aetherion",
      "aliases": ["Emissary of Pure Light"],
      "role": "Eternal Court of Pure Light representative",
      "bio": "An ethereal, aqua-robed angelic emissary who explains the tournament rules in the VIP lounge: no outside interference, no killing outside the pit, and a single favor for bracket winners.",
      "first_appearance_context": "Sipping a crystalline drink in the neutral VIP lounge."
    },
    {
      "name": "Elder Lirael",
      "aliases": [],
      "role": "Verdant Conclave spirit elder",
      "bio": "A graceful spirit elder with living green vines across her skin who laments the tournament's violence and hopes the boy's light is not broken.",
      "first_appearance_context": "Shaking her head in the neutral VIP lounge."
    },
    {
      "name": "Archivist Veyl",
      "aliases": [],
      "role": "Fractured Realms Coalition scholar",
      "bio": "A hooded, multi-eyed intellectual with Neutralization accents who has read sealed reports on Naobito and wants to study him rather than fight him. He predicts the tournament will reveal a new balance.",
      "first_appearance_context": "Adjusting his spectacles in the neutral VIP lounge."
    },
    {
      "name": "Isolde Aster",
      "aliases": ["Sword Saint of Lightning"],
      "role": "Revived fighter; messenger of Hana",
      "bio": "The former Sword Saint of Lightning, dead for ten years and revived by cyan/Malevolence mana. She fights Naobito in a cyan-violet storm dome, delivers Hana's message that the tournament is a filter and the remaining Keys are hidden among the fighters, then whispers 'Pass' when he defeats her.",
      "first_appearance_context": "Stepping out of glowing cyan light in ornate silver-and-cyan plate armor."
    },
    {
      "name": "Sylvara 'Syl' Kane",
      "aliases": ["Key of Echoes", "little echo"],
      "role": "Scavenger from the Fractured Realms; Key of Echoes",
      "bio": "A ragged, terrified scavenger in mismatched tech-gear who is awakened mid-match by Yurei's voice telling her to scream. Her Echo ability produces apocalyptic sonic blasts. Naobito pulls her into his mindscape, bonds with her, and together they create a fused Range Crest that launches the Goliath into deep space.",
      "first_appearance_context": "Shivering in the pit in scavenged tech-gear, moments from being crushed by the Goliath."
    },
    {
      "name": "Kenshi Kashimo",
      "aliases": ["Earth freelancer", "kinetic rat", "little kinetic friend"],
      "role": "Naobito's childhood friend; kinetic anomaly; unexpected ally",
      "bio": "A smug, blue-hooded Earth-born kinetic fighter who travels from Neo-Haven to the arena. His Innate Weave, Over-Rev, lets him push past Mach 5 and convert kinetic force. He threads the needle through Asha's Apex Mantle, fights alongside Naobito/Yurei to a draw, and returns to hide with them in Neo-Haven.",
      "first_appearance_context": "Watching the broadcast in his Neo-Haven apartment, recognizing Naobito."
    },
    {
      "name": "Kurogane Clan Head",
      "aliases": [],
      "role": "Saya's father; Kurogane Clan leader",
      "bio": "Watches Naobito's dominant display from the Kurogane estate with narrowed eyes, declaring that if Naobito returns, Saya will be their bridge or their weapon.",
      "first_appearance_context": "Watching the VeilNet feed in a traditional Japanese estate room."
    },
    {
      "name": "Gorzak the Flayer",
      "aliases": [],
      "role": "Abyssal Dominion Malevolence brute",
      "bio": "A hulking red-skinned brute defeated in the first bout by Lirael Thornvine, who cuts him cleanly in half with a Nature Mana leaf-blade.",
      "first_appearance_context": "Charging Lirael Thornvine in the first official match."
    },
    {
      "name": "VeilNet Anchor",
      "aliases": ["Succubus Anchor", "incubus anchor"],
      "role": "VeilNet broadcast host",
      "bio": "Initially an incubus with glowing red eyes, then shifts mid-broadcast into a stunning succubus with rose-gold eyes and horns, narrating the tournament with predatory excitement and playful sin.",
      "first_appearance_context": "Grinning into the camera as the broadcast opens."
    },
    {
      "name": "Veil Wardens Leader",
      "aliases": [],
      "role": "Leader of the Veil Wardens (neutral enforcers)",
      "bio": "A scarred woman with silver Neutralization Mana who watches the broadcast and warns that the tournament will break the balance, offering sanctuary to Naobito if he wins.",
      "first_appearance_context": "Watching the broadcast in a hidden bunker beneath the city."
    }
  ],
  "factions": [
    {
      "name": "The 12 True Weavers (The Loom)",
      "desc": "The Mistress's enforcers who watch the tournament from VIP thrones. They are divided and increasingly alarmed as Naobito destroys the arena and is revealed to rewrite Yurei's code; Selene ultimately designates him a Class-S Reality Anomaly."
    },
    {
      "name": "Elite Councils of the Nine Realms",
      "desc": "The collective hosts of the Blood Tournament, offering a single favor from the councils to each bracket winner and treating Symbiote-Host pairs as single entries with a delayed bracket."
    },
    {
      "name": "Eternal Court of Pure Light",
      "desc": "Angelic delegates radiating aqua mana; represented by Aetherion, who explains the tournament rules."
    },
    {
      "name": "Abyssal Dominion",
      "desc": "Demon lords pulsing with Malevolence, including Lord Varak and Gorzak the Flayer, who seek to test themselves against the Symbiote-Host pair."
    },
    {
      "name": "Verdant Conclave",
      "desc": "Green-natured spirit elders and fighters like Lirael Thornvine, emphasizing patience, efficiency, and living mana."
    },
    {
      "name": "Silver Veil Enclave",
      "desc": "Neutralization masters in flowing white robes; the Kurogane Clan's broader neutralization tradition belongs here."
    },
    {
      "name": "Fractured Realms Coalition",
      "desc": "Outcasts, rogue vessels, and independent powers; home dimension of Sylvara Kane, where reality was torn apart centuries ago."
    },
    {
      "name": "Kurogane Clan",
      "desc": "Saya's family and traditional Japanese neutralization clan; watches the tournament from a warded estate and plans to use Saya as bridge or weapon."
    },
    {
      "name": "Hart Industries",
      "desc": "Niro Hart's empire; Niro watches the tournament from his private box, growing more interested in Naobito."
    },
    {
      "name": "Veil Wardens (Neutral Enforcers)",
      "desc": "Rogue vessels and independent mages operating from a hidden bunker; they monitor the tournament and offer sanctuary to Naobito if he wins."
    },
    {
      "name": "VeilNet (Underground Broadcast Network)",
      "desc": "The hidden mana-society television network streaming the Blood Tournament across encrypted channels, hosted by the incubus/succubus anchor."
    },
    {
      "name": "Rival Mega-Corporation (Earth)",
      "desc": "A rival Tokyo mega-corp whose CEO watches the feed and plots to kill or recruit Naobito to prevent a Hart alliance."
    }
  ],
  "locations": [
    {
      "name": "Crimson Veil Arena",
      "desc": "A colossal stadium carved from black stone and living shadow hidden beneath three continents, reachable only through Folded gates. It is destroyed when Naobito, Yurei, and Kenshi's final clash shatters its spatial barriers, leaving an open crater under the sky."
    },
    {
      "name": "Deep Space / Void Observatory",
      "desc": "Naobito and Yurei's violet pocket of Corruption Mana where they watch the tournament broadcast, receive Kiritaka's visit, and feel Hana's pull."
    },
    {
      "name": "Ethereal Sanctum",
      "desc": "Hana Yagami's dimension of starlight and cosmic silk where she and Kiritaka observe the fight on ethereal screens and discuss the Hollow Shell."
    },
    {
      "name": "Competitor's Lounge",
      "desc": "A dim, concrete under-arena room where Naobito crashes after his first fight, tended by Saya and analyzed by Reno."
    },
    {
      "name": "Under-Arena Corridors",
      "desc": "Damp tunnels beneath the arena where Naobito, Saya, Sylvara, Reno, and Kenshi regroup between matches."
    },
    {
      "name": "Weavers' VIP Box",
      "desc": "A suspended arc of obsidian thrones where the 12 True Weavers watch, calculate, and are shocked by Naobito's power and Lucien's warmth."
    },
    {
      "name": "Niro's Luxury Box",
      "desc": "A private box on the opposite side where Niro Hart and Mireille Vale watch with wine and obsessive devotion."
    },
    {
      "name": "Kurogane Estate",
      "desc": "A traditional Japanese estate with warded walls where Saya's clan watches the VeilNet feed and plots."
    },
    {
      "name": "Rival Corp Tower (Tokyo)",
      "desc": "A sleek high-rise boardroom where a rival mega-corp CEO watches the feed and plots against Naobito."
    },
    {
      "name": "Veil Wardens Bunker",
      "desc": "A hidden bunker beneath the city where rogue vessels and independent mages monitor the tournament."
    },
    {
      "name": "Primal Expanse",
      "desc": "Asha Nkosi's lush, overgrown jungle domain where she keeps her scars as trophies after the fight."
    },
    {
      "name": "Apex Spire",
      "desc": "The grand hall of the True Weavers where Selene designates Naobito a Class-S Reality Anomaly and Viktor forges reality-binding chains."
    },
    {
      "name": "Chrono-Sanctum",
      "desc": "Lucien Moreau's timeless room of starlight where he moves chess pieces across a multiversal board, ending on Neo-Haven."
    },
    {
      "name": "Neo-Haven, Nevada",
      "desc": "A neon-lit desert city with thin Veil and smuggler Gates; Kenshi's home and later the hiding place of Naobito, Yurei, and Kenshi."
    }
  ],
  "concepts": [
    {
      "term": "Seams",
      "desc": "The unit of mana quantity and density; Reno reports Naobito stabilized at 2.1 million Seams after the fight."
    },
    {
      "term": "Base-Thread (Nature Mana)",
      "desc": "The low-reserve, low-output mana ordinary people run on, colloquially 'green stuff' on Earth, contrasted with fighter-tier mana."
    },
    {
      "term": "Innate Weave (Gimmick)",
      "desc": "A fighter's one signature trick; Kenshi's is kinetic conversion/speed, Naobito's is the Hollow Shell, Asha's is Beast Mana."
    },
    {
      "term": "Over-Rev",
      "desc": "Kenshi Kashimo's kinetic technique that pushes his body past Mach 5, leaving trails of blue plasma and burning his reserves hot and fast."
    },
    {
      "term": "Hollow Shell (K'tai)",
      "desc": "Naobito's technique where black bandages and tentacles erupt and rebuild a housed entity's body around his own architecture, letting him wear Yurei as a biological mech suit and read/rewrite her information."
    },
    {
      "term": "Information Alteration",
      "desc": "Naobito's ability, first used against Asha's Apex Mantle, to rewrite a housed entity's foundational data (density, mana composition) in real time, even phasing them through attacks."
    },
    {
      "term": "Key of Duality",
      "desc": "Naobito's designation as one of six Keys designed by Hana; his role is to align and solve the larger puzzle of reality."
    },
    {
      "term": "Key of Echoes",
      "desc": "Sylvara Kane's hidden designation; her sonic Echo ability and broken geometric node mirror Naobito's, making her the counterpart needed to align the remaining Keys."
    },
    {
      "term": "Fused Range Crest",
      "desc": "A new crest born from Naobito and Sylvara's synced bond, combining six wings with echoing sonic spirals and six eyes, launching the Goliath into deep space."
    },
    {
      "term": "Wild Hunt: Apex Mantle",
      "desc": "Asha Nkosi's named technique: a colossal wave of pure predatory Beast Mana shaped like countless spectral jaws and claws that floods the entire pit."
    },
    {
      "term": "Echo (Sonic) Ability",
      "desc": "Sylvara's awakened power: a raw, apocalyptic sonic scream that warps air, shatters stone, and weaponizes her fear into devastating force."
    },
    {
      "term": "Class-S Reality Anomaly",
      "desc": "Selene's official designation for Naobito after the arena's destruction, sealing the footage to prevent mass panic."
    },
    {
      "term": "Symbiote-Host Bracket",
      "desc": "A tournament bracket treating bonded vessel-and-entity pairs as a single entry, with a slight delay to observe the field."
    },
    {
      "term": "Folded Gates",
      "desc": "Spatial folds used to reach the Crimson Veil Arena and to travel between dimensions; Hana stitches them effortlessly."
    },
    {
      "term": "Corruption Mana",
      "desc": "Yurei's violet, ancient, hungry mana; now wielded in controlled, efficient bursts by the symbiotic pair."
    },
    {
      "term": "Beast Mana",
      "desc": "Asha Nkosi's green-and-gold predatory mana that hardens into living armor of fang and claw and coalesces into spectral predators."
    },
    {
      "term": "Kinetic Mana",
      "desc": "Blue mana that absorbs and converts kinetic force, used by Kenshi to catch projectiles and fuel Over-Rev."
    },
    {
      "term": "Neutralization Mana",
      "desc": "Silver-white mana used to detect, neutralize, and erase mana signatures; Reno packs it in obsidian rounds."
    }
  ],
  "events": [
    {
      "title": "Blood Tournament Opening",
      "summary": "The Crimson Veil Arena opens with thousands of spectators; the 12 True Weavers, Niro Hart, and representatives of the Nine Realms are introduced before the first bouts.",
      "participants": ["VeilNet Anchor", "High Weaver Selene Arkwright", "Niro Hart", "Mireille Vale"]
    },
    {
      "title": "Naobito's Meteor Arrival",
      "summary": "Naobito and Yurei shatter their viewing window and descend from deep space as a blazing violet meteor, cracking the arena floor and announcing the Symbiote-Host bracket.",
      "participants": ["Naobito Yagami", "Yurei Himura"]
    },
    {
      "title": "Hana Yagami's Arrival",
      "summary": "The Mistress of Threads steps into the pit in cyan mana, freezing the arena, and triggers a memory flashback of Naobito's infancy as the first Key.",
      "participants": ["Hana Yagami", "Naobito Yagami", "Yurei Himura"]
    },
    {
      "title": "Naobito vs Lord Varak",
      "summary": "Lord Varak shatters Hana's gate to challenge Naobito, but is systematically dismantled and bound in violet bandages within seconds.",
      "participants": ["Naobito Yagami", "Yurei Himura", "Lord Varak of the Red Abyss", "Hana Yagami"]
    },
    {
      "title": "Isolde Aster's Challenge",
      "summary": "The revived Sword Saint of Lightning fights Naobito in a cyan-violet storm dome, delivers Hana's message that the tournament is a filter and the Keys are hidden among the fighters, and whispers 'Pass' upon defeat.",
      "participants": ["Naobito Yagami", "Yurei Himura", "Isolde Aster"]
    },
    {
      "title": "Hollow Shell Split & Mindscape Bridging",
      "summary": "Yurei is pulled into Naobito's mindscape (a rainy apartment) to bridge broken soul-nodes while Naobito fights Isolde solo, then returns with administrative access and optimized power.",
      "participants": ["Naobito Yagami", "Yurei Himura", "Hana Yagami"]
    },
    {
      "title": "Sylvara's Awakening",
      "summary": "Yurei's voice tells Sylvara to scream; her Echo ability awakens in an apocalyptic sonic blast that staggers the Goliath.",
      "participants": ["Sylvara Kane", "Yurei Himura", "Naobito Yagami"]
    },
    {
      "title": "Fused Range Crest vs Goliath",
      "summary": "Naobito and Sylvara create a fused Range Crest and launch the Goliath several light-years into deep space.",
      "participants": ["Naobito Yagami", "Sylvara Kane", "Yurei Himura"]
    },
    {
      "title": "Mindscape Bonding",
      "summary": "Naobito pulls Sylvara into his mindscape, where she feels like family; they agree to finish the fight together.",
      "participants": ["Naobito Yagami", "Sylvara Kane", "Yurei Himura"]
    },
    {
      "title": "Kenshi's Arrival",
      "summary": "Kenshi Kashimo travels from Neo-Haven via smuggler Gate, breaks into the under-arena corridor, and reunites with Naobito.",
      "participants": ["Kenshi Kashimo", "Naobito Yagami", "Saya Kurogane", "Sylvara Kane", "Reno"]
    },
    {
      "title": "Asha Nkosi's Challenge",
      "summary": "Asha invokes her authority as a True Weaver to turn her match into a 2v1 against Naobito/Yurei and Kenshi, demanding a full-strength fight.",
      "participants": ["Asha Nkosi", "Naobito Yagami", "Yurei Himura", "Kenshi Kashimo"]
    },
    {
      "title": "Hollow Shell vs Asha",
      "summary": "Naobito uses K'tai to house Yurei in a reconstructed body, fighting Asha with scythe, wings, and Kenshi's kinetic support, then rewriting Yurei's code to phase through Apex Mantle.",
      "participants": ["Naobito Yagami", "Yurei Himura", "Kenshi Kashimo", "Asha Nkosi"]
    },
    {
      "title": "Arena Destruction",
      "summary": "The final three-way clash shatters the Crimson Veil Arena's spatial barriers, vaporizing spectator rows and exposing the fight to the open sky.",
      "participants": ["Naobito Yagami", "Yurei Himura", "Kenshi Kashimo", "Asha Nkosi"]
    },
    {
      "title": "Draw Declaration & Class-S Designation",
      "summary": "Selene declares the match a draw and designates Naobito a Class-S Reality Anomaly, sealing the footage.",
      "participants": ["High Weaver Selene Arkwright", "Naobito Yagami", "Yurei Himura", "Kenshi Kashimo", "Asha Nkosi"]
    },
    {
      "title": "Finals Announcement",
      "summary": "Hana declares Naobito already qualified for the finals and places him directly into the Weavers' VIP box, where Lucien shows unprecedented warmth.",
      "participants": ["Hana Yagami", "Naobito Yagami", "Lucien Moreau", "The 12 True Weavers"]
    },
    {
      "title": "Kiritaka's Visit",
      "summary": "Naobito's immortal father appears in deep space, confirms his knowledge of the Key design, expresses pride, and warns that the remaining Keys are waking.",
      "participants": ["Kiritaka Yagami", "Naobito Yagami", "Yurei Himura"]
    },
    {
      "title": "Epilogues",
      "summary": "Asha keeps her scars in the Primal Expanse; Selene designates Naobito Class-S and Viktor forges reality-binding chains while Thorn drafts a chimera; Lucien moves three pieces onto a Neo-Haven square.",
      "participants": ["Asha Nkosi", "High Weaver Selene Arkwright", "Viktor Drago", "Dr. Elias Thorn", "Lucien Moreau"]
    }
  ],
  "quotes": [
    {
      "speaker": "Naobito Yagami",
      "quote": "Our turn."
    },
    {
      "speaker": "Hana Yagami",
      "quote": "Let the real game begin."
    },
    {
      "speaker": "Naobito Yagami",
      "quote": "I don't care if you're my mother, Mistress."
    },
    {
      "speaker": "Hana Yagami",
      "quote": "You will address me as 'Ka-san' if speaking directly to me. And if you cannot respect me as a mother... respect me as an elder."
    },
    {
      "speaker": "Naobito Yagami",
      "quote": "Your power is loud. But it's empty."
    },
    {
      "speaker": "Naobito Yagami",
      "quote": "Tell her... I'm not her puzzle anymore. I'm the one who solves it."
    },
    {
      "speaker": "Isolde Aster",
      "quote": "Pass."
    },
    {
      "speaker": "Yurei Himura",
      "quote": "System online, little lamb. Give her hell."
    },
    {
      "speaker": "Naobito Yagami",
      "quote": "I'm not waiting for the finals."
    },
    {
      "speaker": "Yurei Himura",
      "quote": "Breathe, little echo. We've got you."
    },
    {
      "speaker": "Naobito Yagami",
      "quote": "Stay behind me. We'll finish this together."
    },
    {
      "speaker": "Kenshi Kashimo",
      "quote": "My best friend's got a date with a goddess. I'm just the plus-one."
    },
    {
      "speaker": "Asha Nkosi",
      "quote": "Come, little vessel. Come, loud Earth boy. Show me everything you have."
    },
    {
      "speaker": "Asha Nkosi",
      "quote": "YES! BREAK IT ALL! LET'S SEE WHO SURVIVES THE FALL!"
    },
    {
      "speaker": "Asha Nkosi",
      "quote": "Well fought... both of you."
    },
    {
      "speaker": "Lucien Moreau",
      "quote": "Tell me... how many of you still believe the boy is merely a fragile host being controlled by his Dark Maiden?"
    },
    {
      "speaker": "Naobito Yagami",
      "quote": "I was expecting to get executed, not adopted."
    },
    {
      "speaker": "Kenshi Kashimo",
      "quote": "Your mom's a goddess, your dad's immortal, and now the Beast Weaver wants to throw hands for fun. Your life is insane, Nao."
    },
    {
      "speaker": "Yurei Himura",
      "quote": "She's testing us... separately."
    },
    {
      "speaker": "Naobito Yagami",
      "quote": "I'm done being the boy everyone ignores."
    },
    {
      "speaker": "Lucien Moreau",
      "quote": "Your move, little anomaly."
    },
    {
      "speaker": "Hana Yagami",
      "quote": "Prove to them why I chose you."
    }
  ],
  "relationships": [
    {
      "pair": "Naobito Yagami & Yurei Himura",
      "note": "Deepened symbiosis: they now fight as a single Hollow Shell, with Naobito housing and rewriting Yurei's code while she guides and supports him; trust replaces possession."
    },
    {
      "pair": "Naobito Yagami & Hana Yagami",
      "note": "Mother and son: Hana reveals herself as the Mistress and Naobito's mother, triggering his infant memory; she tests and proudly watches him while he refuses to be her puzzle."
    },
    {
      "pair": "Naobito Yagami & Kiritaka Yagami",
      "note": "Father and son: Kiritaka confirms he knew of the Key design, expresses pride, warns of waking Keys, and teases Yurei before vanishing."
    },
    {
      "pair": "Naobito Yagami & Kenshi Kashimo",
      "note": "Childhood friends reunited: Kenshi travels across dimensions to back Naobito up, fights beside him to a draw against Asha, and hides with him in Neo-Haven."
    },
    {
      "pair": "Naobito Yagami & Sylvara Kane",
      "note": "Key of Duality and Key of Echoes: bonded through a mindscape meeting and a fused Range Crest, becoming the first two aligned Keys."
    },
    {
      "pair": "Naobito Yagami & Lucien Moreau",
      "note": "Mentor and vessel: Lucien shows unprecedented paternal warmth, gives Naobito a throne among the Weavers, and moves him onto his multiversal chessboard."
    },
    {
      "pair": "Naobito Yagami & Asha Nkosi",
      "note": "Rival respect: Asha fights them at full strength and, after being forced defensive, acknowledges them as worthy opponents worth keeping alive."
    },
    {
      "pair": "Naobito Yagami & Saya Kurogane",
      "note": "Empathetic bond continues: Saya tends his wounds, reminds him he is human, and scolds him for nearly dying while being relieved he survived."
    },
    {
      "pair": "Yurei Himura & Hana Yagami",
      "note": "Mutual respect: Yurei calls Hana a true weaver who knows what she made, and Hana's test forces Yurei to accept Naobito rewriting her code."
    },
    {
      "pair": "Yurei Himura & Sylvara Kane",
      "note": "Maiden and echo: Yurei awakens Sylvara's Echo with a single command and calls her 'little echo,' guiding the new Key."
    },
    {
      "pair": "Niro Hart & Mireille Vale",
      "note": "Master and devotee: Mireille offers to kill threats to Niro, who treats her as a dangerous pet while growing more interested in Naobito."
    },
    {
      "pair": "Reno & Lady Elara Vane",
      "note": "Weaver and pawn: Reno reports Naobito's stabilized stats to Elara, who smiles thinly and treats her pawn as a measuring tool."
    },
    {
      "pair": "Kenshi Kashimo & Asha Nkosi",
      "note": "Speed vs Beast: Kenshi threads the needle through her Apex Mantle, earning her grudging respect and a kinetic scar she keeps."
    }
  ]
}

with open(r"D:\develop\override-codex\extract_3.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("written")
print({k: len(v) if isinstance(v, list) else v for k, v in data.items()})
