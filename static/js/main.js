Amplitude.init({
    "bindings": {
        37: 'prev',
        39: 'next',
        32: 'play_pause'
    },
    "songs": [
        {
            "name": "food is not the enemy",
            "artist": "kevin",
            "album": "demos",
            "url": "../media/audio/food is not the enemy.mp3",
            "cover_art_url": "../static/images/song1.jpg",
        },
        {
            "name": "garden",
            "artist": "kevin",
            "album": "demos",
            "url": "../media/audio/garden.mp3",
            "cover_art_url": "../static/images/song2.jpg",
        },
    ]
});

window.onkeydown = function(e) {
    return !(e.keyCode == 32);
};

/*
    Handles a click on the song played progress bar.
    */
document.getElementById('song-played-progress-1').addEventListener('click', function( e ){

    if( Amplitude.getActiveIndex() == 0){
        var offset = this.getBoundingClientRect();
        var x = e.pageX - offset.left;

        Amplitude.setSongPlayedPercentage( ( parseFloat( x ) / parseFloat( this.offsetWidth) ) * 100 );
    }
});

document.getElementById('song-played-progress-2').addEventListener('click', function( e ){

    if( Amplitude.getActiveIndex() == 1){
        var offset = this.getBoundingClientRect();
        var x = e.pageX - offset.left;

        Amplitude.setSongPlayedPercentage( ( parseFloat( x ) / parseFloat( this.offsetWidth) ) * 100 );
    }
});


