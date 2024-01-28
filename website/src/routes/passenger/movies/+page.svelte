<script>
    import CardCarousel from "../../../components/CardCarousel.svelte";
    import NavBar from "../../../components/NavBar.svelte";

    let cards = [
        {
            title: 'Ted',
            description: 'A comedy film directed by Seth MacFarlane about a grown man named John Bennett whose childhood teddy bear, Ted, magically comes to life. The movie follows their misadventures as they navigate adulthood together while dealing with the consequences of Ted's crude and inappropriate behavior.',
            status: false,
            src: "https://m.media-amazon.com/images/I/41DsVUWsCLL._AC_UF894,1000_QL80_.jpg"
        },
        {
            title: 'Over the Hedge',
            description: 'An animated comedy film about a group of woodland creatures, including a raccoon named RJ and a turtle named Verne, who venture into the suburbs to gather food. Along the way, they encounter various challenges and learn about friendship, family, and the importance of community.',
            status: false,
            src: "https://m.media-amazon.com/images/I/516V1BUK6xL._AC_UF894,1000_QL80_.jpg"
        },
        {
            title: 'Top Gun: Maverick',
            description: 'An action drama film and sequel to the 1986 film "Top Gun." Directed by Joseph Kosinski, it follows Pete "Maverick" Mitchell, now a flight instructor, as he trains a new generation of Top Gun pilots while confronting his past and legacy as one of the Navy's top aviators.',
            status: false,
            src: "https://i5.walmartimages.com/seo/Top-Gun-Maverick-Movie-Poster-Quality-Glossy-Print-Photo-Wall-Art-Tom-Cruise-Jennifer-Connelly-Size-24x36_bbb92289-b359-423e-a8fe-6142b188f677.4da7e4af2871002298f4804afb44b955.jpeg" },
        {
            title: 'Hacksaw Ridge',
            description: 'A biographical war drama directed by Mel Gibson, based on the true story of Desmond Doss, a conscientious objector who served as a combat medic during World War II. The film depicts Doss's remarkable bravery and heroism as he saves 75 soldiers without firing a single shot during the Battle of Okinawa, despite facing intense opposition due to his refusal to carry a weapon.',
            status: false,
            src: "https://m.media-amazon.com/images/I/71Tpd21hEbL._AC_UF894,1000_QL80_.jpg" },
        {
            title: 'Super Mario Bros',
            description: 'A live-action fantasy adventure film loosely based on the popular video game franchise of the same name. Directed by Annabel Jankel and Rocky Morton, the movie follows Mario and Luigi, two plumbers from Brooklyn, as they travel to an alternate dimension inhabited by dinosaurs ruled by the villainous King Koopa. They must rescue Princess Daisy and save both worlds from Koopa's evil plans.',
            status: false,
            src: "https://m.media-amazon.com/images/I/91zqGNzwk5L._AC_UF894,1000_QL80_.jpg" },
        {
            title: 'Barbie',
            description: 'A live-action film starring Margot Robbie as the iconic doll character. The movie follows Barbie as she embarks on a modern-day adventure, navigating through the ups and downs of life in pursuit of her dreams. With Margot Robbie's charm and humor, "Barbie" promises to be a fun and empowering story for audiences of all ages.',
            status: false,
            src: "https://m.media-amazon.com/images/I/71BgdzmFDAL._AC_UF894,1000_QL80_.jpg" },
        {
            title: 'Avengers Endgame',
            description: 'A superhero film directed by Anthony and Joe Russo and produced by Marvel Studios. It serves as the culmination of the Marvel Cinematic Universe's Infinity Saga. The film follows the remaining Avengers as they assemble one last time to undo the devastating effects of Thanos' snap, known as the Decimation, and restore balance to the universe. Packed with action, drama, and emotional moments, "Avengers: Endgame" brings the epic story arc of the MCU to a thrilling and satisfying conclusion.',
            status: false,
            src: "https://i.pinimg.com/originals/66/bd/9b/66bd9b1f8354a9aa6900dee35bc2a911.jpg" },
        {
            title: 'Minions',
            description: 'An animated comedy film and a spin-off/prequel to the "Despicable Me" franchise. Directed by Pierre Coffin and Kyle Balda, the film explores the origin story of the yellow, pill-shaped Minions, who have existed since the beginning of time and seek to serve the most despicable master they can find. Set in the 1960s, the film follows three Minions—Kevin, Stuart, and Bob—as they embark on a journey to find a new master and end up working for the supervillain Scarlet Overkill. Full of humor, slapstick comedy, and adorable moments, "Minions" is a family-friendly adventure that showcases the beloved characters in their own hilarious escapades.',
            status: false,
            src: "https://i.etsystatic.com/41716657/r/il/9c990a/4742863548/il_570xN.4742863548_patj.jpg" },
        {
            title: 'Garfield',
            description: 'A live-action/CGI comedy film based on the popular comic strip character Garfield, created by Jim Davis. Directed by Peter Hewitt, the film follows the lasagna-loving, sarcastic orange tabby cat named Garfield, voiced by Bill Murray, as he gets into mischief and schemes to rescue his canine friend Odie from a television celebrity who plans to use him for a dog show. Garfield's antics and humor drive the plot as he navigates through various comedic situations while learning valuable lessons about friendship and responsibility.',
            status: false,
            src: "https://m.media-amazon.com/images/I/51b6mLCvBuL._AC_UF894,1000_QL80_.jpg" },
        {
            title: 'Shrek2',
            description: 'An animated comedy film and the sequel to the highly successful "Shrek" movie. Directed by Andrew Adamson, Kelly Asbury, and Conrad Vernon, the film follows the ogre Shrek and his wife Fiona as they travel to the kingdom of Far Far Away to meet Fiona's parents, King Harold and Queen Lillian. However, their visit takes an unexpected turn when they encounter Prince Charming, who is determined to win Fiona's hand in marriage. Packed with humor, memorable characters, and pop culture references, "Shrek 2" is a fun-filled adventure that explores themes of love, acceptance, and self-discovery.',
            status: false,
            src: "https://m.media-amazon.com/images/M/MV5BMDJhMGRjN2QtNDUxYy00NGM3LThjNGQtMmZiZTRhNjM4YzUxL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg" },
        {
            title: 'Baby Driver',
            description: 'An action-packed crime film directed by Edgar Wright. It follows Baby, a talented getaway driver with tinnitus, who works for a crime boss named Doc. When Baby falls in love and wants to leave the criminal life behind, he's pulled back in for one last job. The film is known for its stylish action sequences, thrilling car chases, and an outstanding soundtrack.',
            status: false,
            src: "https://m.media-amazon.com/images/I/91K98RNBBWL.jpg" },
        {
            title: 'Despicable Me 3 ',
            description: 'An animated comedy film where former supervillain Gru teams up with the Anti-Villain League to stop a new threat posed by a former child star turned supervillain named Balthazar Bratt. Gru also discovers he has a long-lost twin brother named Dru, leading to a family dynamic shift and comedic adventures.',
            status: false,
            src: "https://m.media-amazon.com/images/I/61f1bYNLpKL._AC_UF1000,1000_QL80_.jpg" },
        {
            title: 'Spaceballs',
            description: 'A sci-fi comedy film directed by Mel Brooks. A spoof of the "Star Wars" franchise, the movie follows Lone Starr and his sidekick Barf as they embark on a quest to rescue Princess Vespa from the evil Dark Helmet. Packed with hilarious gags, memorable characters, and satirical humor, "Spaceballs" is a beloved cult classic in the realm of parody films.',
            status: false,
            src: "https://m.media-amazon.com/images/I/71U8fIXlGHL._AC_UF894,1000_QL80_.jpg" },
        {
            title: 'Mission Impossible',
            description: 'An action spy film directed by Brian De Palma. It follows Ethan Hunt, an IMF agent framed for the deaths of his team during a mission gone wrong. Ethan must uncover the real traitor and clear his name while navigating a web of deception and high-stakes espionage. Packed with thrilling action sequences and suspenseful twists, "Mission: Impossible" is a gripping entry in the spy thriller genre.',
            status: false,
            src: "https://m.media-amazon.com/images/I/A1M0qlxNo6L.jpg" },
        {
            title: 'The Secret Life of Pets',
            description: 'An action spy film directed by Brian De Palma. It follows Ethan Hunt, an IMF agent framed for the deaths of his team during a mission gone wrong. Ethan must uncover the real traitor and clear his name while navigating a web of deception and high-stakes espionage. Packed with thrilling action sequences and suspenseful twists, "Mission: Impossible" is a gripping entry in the spy thriller genre.',
            status: false,
            src: "https://m.media-amazon.com/images/I/81ZCRFRoXYL._AC_UF894,1000_QL80_.jpg" },
        {
            title: 'Totoro',
            description: 'A charming animated film directed by Hayao Miyazaki. It follows two sisters who encounter magical creatures called Totoros in the countryside. The film showcases their enchanting adventures and teaches valuable lessons about family, friendship, and imagination.',
            status: false,
            src: "https://m.media-amazon.com/images/I/81oON83v4WL._AC_UF894,1000_QL80_.jpg" },
        {
            title: 'Knives Out',
            description: 'A mystery film directed by Rian Johnson. After the wealthy patriarch of a dysfunctional family dies, a detective named Benoit Blanc investigates his death, which was initially deemed a suicide. As Blanc delves deeper into the family's secrets and conflicting motives, tensions rise and suspects emerge. Filled with twists, humor, and a stellar ensemble cast, "Knives Out" is a clever and entertaining whodunit that keeps audiences guessing until the very end.',
            status: false,
            src: "https://pbncanvas.com/wp-content/uploads/2022/02/Knives-Out-movie-poster-paint-by-numbers.jpg" },
        {
            title: 'Birds of Prey',
            description: 'An action film directed by Cathy Yan. After breaking up with the Joker, Harley Quinn teams up with a group of fierce female superheroes to protect a young girl from a crime lord. Packed with stylish action sequences and witty humor, "Birds of Prey" is a fun and empowering ride through Gotham City.',
            status: false,
            src: "https://m.media-amazon.com/images/I/61c11xwXFjL._AC_UF894,1000_QL80_.jpg" },
        {
            title: 'It',
            description: 'A horror film directed by Andy Muschietti, based on the novel by Stephen King. Set in the town of Derry, Maine, the film follows a group of kids known as the Losers' Club as they confront an ancient evil entity that takes the form of a malevolent clown named Pennywise. As they face their deepest fears, the Losers' Club must band together to defeat Pennywise and put an end to its reign of terror. Packed with scares and suspense, "It" is a chilling adaptation that keeps audiences on the edge of their seats.',
            status: false,
            src: "https://i.ebayimg.com/images/g/qHwAAOSw1Y5dcuMC/s-l1600.jpg" },
    ]
</script>

<div class="card-carousel">
    <CardCarousel cards={cards} />
</div>