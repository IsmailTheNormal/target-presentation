define('layoutcontrols/menuPointerMarker', function () {
  'use strict';
  var dataKey = 'data-header-menu-point-marker-key';
  function getKeyValue(elem) {
    return elem.dataset.headerMenuPointMarkerKey;
  }

  function initMarkers() {
    document.querySelectorAll('div[' + dataKey + ']')
      .forEach(function(m) {
        if (!localStorage.getItem(getKeyValue(m))) {
          m.innerHTML = '&nbsp;'; //FF fix
          m.classList.remove('header-menu__hidden');
          m.classList.remove('header-submenu__hidden');
        }
      });
  }

  function checkCommunityPage() {
    var communityPage = window.location.pathname.startsWith('/communities');
    var parentsPage = window.location.pathname.startsWith('/parents');
    if (communityPage || parentsPage) {
      document.querySelectorAll('div[' + dataKey + ']').forEach(function (marker) {
        var key = getKeyValue(marker);
        var communityPageViewed = communityPage && key.startsWith('header-menu_point-marker_close_user_');
        var parentsPageViewed = parentsPage && key.startsWith('header-menu_parents-point-marker_close_user_');
        if ((communityPageViewed || parentsPageViewed) && !localStorage.getItem(key)) {
          localStorage.setItem(key, Date.now());
        }
      });
    }
  }

  return {
    init: function () {
      checkCommunityPage();
      initMarkers();
    }
  };
});
