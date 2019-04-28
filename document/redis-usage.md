1. installation of redis
    * install brew
        <p>
        <code>
            $ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
        </code>
        <p>
    * install redis
        <p>
        <code>
            $ brew install redis
        </code>
        </p>
2. start redis, defult port is 6379
    <p>
    <code>
        $ brew services start redis
    </code>
    </p>

3. shell
    <p>
    <code>
        $ redis-cli
    </code>
    </p>
    <p>
    <code>
        >>> keys *
    </code>
    </p>