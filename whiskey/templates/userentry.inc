<a href="{{ url_for('profile', nickname = user['nickname']) }}">
  <div class="userentry">
    <img src="{{ user.avatar(64) }}" alt="{{ user['fullname'] }}" class="smallavatar" />       <!-- <p id="uenickname">{{ user['nickname'] }}</p> -->
    <p class="uefullname">{{ user['fullname'] }}</p>
  </div>
</a>
