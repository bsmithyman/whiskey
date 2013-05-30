<div class="authorbio">
<img src="{{ author.avatar(128) }}" class="bioavatar" />
<p>{{ author['fullname'] }}</p>
<a href="{{ url_for('profile', nickname = author['nickname']) }}" class="yui3-button yui3-button-small">Profile</a>
<a href="mailto:{{ author['email'] }}" class="yui3-button yui3-button-small yui-3-button-secondary">Email</a>
</div>
