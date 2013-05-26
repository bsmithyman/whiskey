var sitetext = '{{ pageinfo['sitename'] }}';
document.ready = function (){
    var siteheader = $('#sitename');
    siteheader.text("");

    jQuery({count:0}).animate({count:sitetext.length}, {
        duration: 3000,
        step: function () {
            siteheader.text(sitetext.substring(0, Math.round(this.count)));
        }
    });
};
