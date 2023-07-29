# Ping CRM

A demo application to illustrate how Inertia.js works with [Flask](http://flask.pocoo.org/)
and [Vue 3](https://v3.vuejs.org/).

![](https://raw.githubusercontent.com/inertiajs/pingcrm/master/screenshot.png)

> This is a port of the original [Ping CRM](https://github.com/inertiajs/pingcrm)
> written in Laravel and Vue.

# Installation

Clone the repo locally:

```
git clone https://github.com/rr0001/pingcrm-flask.git
cd pingcrm-flask
```

Install dependencies:

```
poetry install
poetry shell
poe init
poe migrate
```

Run database seeder:

```
poe seed
```

Run dev server:

```
poe dev
```
