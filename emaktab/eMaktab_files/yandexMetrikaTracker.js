define('ab/yandexMetrikaTracker', ['common/dnevnik'], function () {
    'use strict';

    return function (model) {
        var selector = ' .ya-metrika-trackable';
        if (model.rootElementId) {
          selector = '#' + model.rootElementId + selector;
        }

        var action = model.action,
            trackableElements = document.querySelectorAll(selector),
            metrikaIds = dnevnik.settings.yandexMetrikaIds,
            reachGoalAction = function (element) {
                element.addEventListener('click', function () {
                    var target = element.getAttribute('data-target');
                    if (target) {
                      metrikaIds.forEach(metrikaId => {
                        var counter = window['yaCounter' + metrikaId];
                        if (counter && counter.reachGoal) {
                          counter.reachGoal(target);
                        }
                      });
                    }
                });
            },
            actionFunction;

        switch (action) {
            case 'reachGoal':
                actionFunction = reachGoalAction;
        }

        [].forEach.call(trackableElements, function (element) {
            if (actionFunction) {
                actionFunction(element);
            }
        });
    };
});
