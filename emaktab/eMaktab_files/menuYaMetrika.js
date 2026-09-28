/* eslint-disable */
define('analytics/menuYaMetrika', ['analytics/yaMetrikaTracker'], function (tracker) {
  'use strict';

  function sendSchoolPayments(action) {
    var timestamp = Date.now();
    var userId = (dnevnik.user && dnevnik.user.id) || '0';
    var params = {};

    params.school_payments_assignments_availability = {};
    params.school_payments_assignments_availability[timestamp] = {};
    params.school_payments_assignments_availability[timestamp][userId] = {};
    params.school_payments_assignments_availability[timestamp][userId][action] = null;

    tracker.params(params);
  }

  function send(e) {
    var role = (dnevnik.user && dnevnik.user.commonRole) || '';
    var timestamp = Date.now();
    var userId = (dnevnik.user && dnevnik.user.id) || '0';
    var path = window.location.pathname;
    var link = e.target.pathname;

    var params = {};
    params.Menu = {};
    params.Menu[timestamp] = {};
    params.Menu[timestamp][userId] = {};
    params.Menu[timestamp][userId][role] = {};
    params.Menu[timestamp][userId][role].click = {};
    params.Menu[timestamp][userId][role].click[path] = {}; 
    params.Menu[timestamp][userId][role].click[path][link] = null;

    tracker.params(params);
  }

  $('.header-menu a').click(send);

  var schoolPaymentsMenuItem = $('.header-menu__payments');
  if (schoolPaymentsMenuItem.length) {
    sendSchoolPayments('view_account_point');
    schoolPaymentsMenuItem.click(function () {
      sendSchoolPayments('click_account_point');
    });
  }
});
