<div class="shortpost">
    <img src="{{ author.avatar(64) }}" class="smallavatar" />
    <p class="posttitle"><a href="{{ url_for('post', identifier = post['_id']) }}">{{ post['title'] }}</a></p>
    <p class="postauthor"><a href="{{ url_for('profile', nickname = author['nickname']) }}">{{ author['fullname'] }}</a></p>
    <p class="postslug">{{ post['slug'] }}</p>
</div>
