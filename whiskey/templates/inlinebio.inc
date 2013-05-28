<div class="authorbio">
<img src="{{ author.avatar(128) }}" class="bioavatar" />
<p>{{ author['fullname'] }}</p>
<a href="{{ url_for('profile', nickname = author['nickname']) }}">
  <div class="button">Profile</div>
</a>
<a href="mailto:{{ author['email'] }}">
  <div class="button">Email</div>
</a>
</div>
