'use strict';

angular.module('bulbs.externalLink.edit', [])
  .directive('externalLinkEdit', [
    function () {
      restrict: 'E',
      template: '/cms/partials/external-link/external-link-edit.html',
      scope: {
        article: '='
      }
    }
  ]);
