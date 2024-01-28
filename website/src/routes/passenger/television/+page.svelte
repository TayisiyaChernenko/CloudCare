<script>
    import CardCarousel from "../../../components/CardCarousel.svelte";
    import NavBar from "../../../components/NavBar.svelte";

    let cards = [ 
        {
            title: 'Breaking Bad",
            description: 'A high school chemistry teacher turned methamphetamine manufacturer navigates the criminal underworld.',
            status: false,
            src: "https://flxt.tmsimg.com/assets/p185846_b_v8_ad.jpg"
        },
        {
            title: 'The Office',
            description: 'A mockumentary-style sitcom that follows the daily lives of office employees working at Dunder Mifflin's Scranton, Pennsylvania branch.',
            status: false,
            src: "https://mypostercollection.com/wp-content/uploads/2019/06/the-office-poster-1.jpg"
        },
        {
            title: 'Stranger Things',
            description: 'Set in the 1980s, this series follows a group of kids who encounter supernatural forces and government conspiracies in their small town.',
            status: false,
            src: "https://i5.walmartimages.com/asr/4d6f3d48-bc1d-4844-9653-2da626b80ef3_1.7b77e5d59b2f72ff55664f65327dd07a.jpeg"
             },
        {
            title: 'Mindhunter',
            description: 'Based on true events, this series follows FBI agents as they interview serial killers to understand their psychology and solve ongoing cases.',
            status: false,
            src: "https://image.tmdb.org/t/p/original/cVRAYMXWBtmkEBGa44GRV1Ms3tV.jpg" },
        {
            title: 'The Mandalorian',
            description: 'Set in the Star Wars universe, this series follows a lone bounty hunter as he navigates the outer reaches of the galaxy.',
            status: false,
            src: "https://salidaetc.com/wp-content/uploads/2020/01/The-Mandalorian.jpg" },
        {
            title: 'The Crown',
            description: 'This biographical drama chronicles the reign of Queen Elizabeth II, from her wedding in 1947 to the present day.',
            status: false,
            src: "https://image.tmdb.org/t/p/original/xoRYlOQMCooz3jcwdtt348qB9oj.jpg" },
        {
            title: 'Pride and Prejudice',
            description: 'A classic adaptation of Jane Austen's novel, this mini-series follows the tumultuous relationship between Elizabeth Bennet and Mr. Darcy in 19th century England.',
            status: false,
            src: "https://alchetron.com/cdn/pride-and-prejudice-1995-tv-series-e31becc4-272f-4ac0-a55e-6b396c90983-resize-750.jpeg" },
        {
            title: 'The Witcher',
            description: 'Based on the book series by Andrzej Sapkowski, this fantasy series follows Geralt of Rivia, a monster hunter known as a Witcher, as he navigates a world filled with supernatural beings, political intrigue, and moral ambiguity.',
            status: false,
            src: "https://tse4.mm.bing.net/th?id=OIP.R7qVsA4aqAqOnGSQjihrXwHaLH&pid=Api" },
        {
            title: 'Doctor Who',
            description: 'A British sci-fi series following the adventures of the Doctor, a time-traveling alien, and his companions as they explore the universe, battle villains, and save civilizations aboard the TARDIS, a spaceship disguised as a British police box.',
            status: false,
            src: "https://fanaru.com/doctor-who/image/7739-doctor-who-doctor-who-poster.jpg" },
        {
            title: 'My Little Pony: Friendship is Magic',
            description: 'An animated series that follows the adventures of Twilight Sparkle and her friends, known as the Mane Six, as they learn about the magic of friendship in the colorful land of Equestria. Through their adventures, they encounter challenges, make new friends, and learn valuable lessons about loyalty, honesty, kindness, generosity, laughter, and magic.',
            status: false,
            src: "https://picfiles.alphacoders.com/959/thumb-1920-95981.jpg" },
    ]
</script>

<div class="card-carousel">
    <CardCarousel cards={cards} />
</div>