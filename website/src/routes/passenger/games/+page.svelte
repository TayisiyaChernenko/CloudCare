<script>
    import CardCarousel from "../../../components/CardCarousel.svelte";
    import NavBar from "../../../components/NavBar.svelte";

    let cards = [
       {
            title: 'Candy Crush',
            description: 'A Colorful Challenge Game',
            status: false,
            src: "https://k1.midasplayer.com/images/share/banners/candycrush.png?_v=kmoqjd"
        },
        {
            title: 'Chess',
            description: 'All Levels Strategy Game',
            status: false,
            src: "https://www.chess-space.com/wp-content/uploads/2012/11/CHESS.png"
        },
        {
            title: 'Checkers',
            description: 'Fun for kids',
            status: false,
            src: "https://www.casualarena.com/bundles/app/st/games/che/fb/casualarena-fb-en.jpg?4188916" },
        {
            title: 'Sudoko',
            description: 'A Numbers Brain-Puzzle Game',
            status: false,
            src: "https://www.my-sudoku.com/images/snap_banner.jpg" },
        {
            title: 'Crossy Road',
            description: 'Fun and Simple',
            status: false,
            src: "https://mobiledevmemo.com/wp-content/uploads/2015/04/crossy_road.jpg" },
        {
            title: 'Cross Word',
            description: 'A Word-Based Brain Teaser',
            status: false,
            src: "https://play-lh.googleusercontent.com/DjuowCxLuHPSUrqfkXEjlYB92VUnvHWctWOS8WyC437G-LT-aNSepN30D7NtecfkQ2c" },
        {
            title: 'Poker',
            description: 'A Game of Wits',
            status: false,
            src: "https://smartcasinoguide.com/app/uploads/2018/01/Casino-hold-em-poker-casino-holdem-bonus-bet-online-gameplay-table.jpg" },
        {
            title: 'Pool',
            description: 'A Game of Geometry and Precision',
            status: false,
            src: "https://games.lol/wp-content/uploads/2019/07/pool-billiards-pro-pc-full-version.jpg" },
    ]
</script>

<div class="card-carousel">
    <CardCarousel cards={cards} />
</div>