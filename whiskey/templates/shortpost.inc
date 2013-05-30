  <div class="l-box">
    <img src="{{ author.avatar(72) }}" class="yui3-img-rounded leftimg" />
    <h2>{{ post['title'] }}</h2>
    <p>by <a href="{{ url_for('profile', nickname = author['nickname']) }}">{{ author['fullname'] }}</a></p>
    <blockquote>
      {{ post['slug'] }}<br />
      <a href="{{ url_for('post', identifier = post['_id']) }}">Read more...</a>
    </blockquote>
  </div>
