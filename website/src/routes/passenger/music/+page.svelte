<script>
    import CardCarousel from "../../../components/CardCarousel.svelte";
    import NavBar from "../../../components/NavBar.svelte";

    let cards = [
       {
            title: 'Blinding Lights',
            description: 'The Weeknd',
            status: false,
            src: "https://images.genius.com/abb1ae358cc3cdda3195a8228143446a.770x770x1.jpg"
        },
        {
            title: 'Three Little Birds',
            description: 'Bob Marley & The Wailers',
            status: false,
            src: "https://4.bp.blogspot.com/-wepH8lvYPTk/UI1qHS-Y-lI/AAAAAAAACWU/211f3uTKZwQ/s400/three+little+birds+bob+marley+0.png"
        },
        {
            title: 'Bad Medicine',
            description: 'Bon Jovi',
            status: false,
            src: "https://1.bp.blogspot.com/-Kh0LbRthJ3c/Tey54XMSrdI/AAAAAAAAAfw/AgkOA9A6SPM/s1600/bad+medicine+us+promo.JPG" },
        {
            title: 'Teenage Dream',
            description: 'Katy Perry',
            status: false,
            src: "https://i.pinimg.com/originals/21/44/d1/2144d1dc8463a652bcfc661249ab8866.jpg" },
        {
            title: 'Titanium',
            description: 'David Guetta',
            status: false,
            src: "https://1.bp.blogspot.com/-xX7kOYLsKbM/TkAY0lEw0MI/AAAAAAAAATQ/4IaMEcZUdNw/s1600/00-david_guetta_and_sia_-_titanium-web-2011-cover-zzzz.jpg" },
        {
            title: 'Sunny',
            description: 'Bobby Hebb',
            status: false,
            src: "https://i.discogs.com/wC7IRBerLbdYdtM6csMfHXF_wt3T4O0b9aSabwosZX4/rs:fit/g:sm/q:90/h:568/w:585/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9SLTU3Nzg2/ODItMTQwMjQxMTE3/OC01Mjk4LmpwZWc.jpeg" },
        {
            title: 'Miss Jackson',
            description: 'Panic at the Disco',
            status: false,
            src: "https://i.pinimg.com/originals/c5/00/53/c50053d754e28c22e21f5e51e4ef14a1.jpg" },
        {
            title: 'The Nights',
            description: 'Avicci',
            status: false,
            src: "https://mir-s3-cdn-cf.behance.net/project_modules/hd/73ab9c74461913.5c30aab0bfca5.jpg" },
        {
            title: 'Free Bird',
            description: 'Lynyrd Skynyrd',
            status: false,
            src: "https://i.discogs.com/GcW9S74Gvwa9nSvX2q2K54iHxMwLSHb6vuqR10wdaQA/rs:fit/g:sm/q:90/h:600/w:594/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9SLTI2MTI2/MzItMTI5MzI4NTU4/My5qcGVn.jpeg" },
        {
            title: 'Let it Go',
            description: 'Idina Menzel',
            status: false,
            src: "https://www.crownnote.com/sites/default/files/11660886813_344f3a7bd4_o.png" },
    ]
</script>

<div class="card-carousel">
    <CardCarousel cards={cards} />
</div>