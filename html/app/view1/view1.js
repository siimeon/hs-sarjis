'use strict';

angular.module('myApp.view1', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
    $routeProvider.when('/comic', {
      templateUrl: 'view1/view1.html',
      controller: 'View1Ctrl'
    });
}])

.controller('View1Ctrl', ["$scope", "$http", function($scope, $http){
    $http.get("data.json")
      .then(function (response) {
        $scope.name = response.data.name;
        $scope.url = response.data.url;
      });
}]);