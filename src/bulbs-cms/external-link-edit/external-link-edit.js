'use strict';

angular.module('bulbs.externalLink.edit', [])
  .directive('externalLinkEdit', [
    function () {
      return {
        restrict: 'E',
        templateUrl: '/cms/partials/externallink/external-link-edit.html',
        scope: {
          article: '='
        }
      };
    }
  ]);
