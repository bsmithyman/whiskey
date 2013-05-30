  <div class="l-box">
    <img src="{{ author.avatar(75) }}" class="yui3-img-rounded leftimg" />
    <h2>{{ post['title'] }}</h2>
    <p><a href="{{ url_for('profile', nickname = author['nickname']) }}" class="yui3-badge-info">{{ author['fullname'] }}</a></p>
    <blockquote>
      {{ post['slug'] }}<br />
      <a href="{{ url_for('post', identifier = post['_id']) }}">Read more</a>
    </blockquote>
  </div>
