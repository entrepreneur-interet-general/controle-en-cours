var myApp = angular.module("myApp", ["ngRoute", "ngResource", "myApp.services"]);

var services = angular.module("myApp.services", ["ngResource"])
services
// .factory('Work', function($resource) {
//     return $resource('http://localhost:5000/api/v1/works/:id', {id: '@id'}, {
//         get: { method: 'GET' },
//         delete: { method: 'DELETE' }
//     });
// })
// .factory('Works', function($resource) {
//     return $resource('http://localhost:5000/api/v1/works', {}, {
//         query: { method: 'GET', isArray: true },
//         create: { method: 'POST', }
//     });
// })
// .factory('Juridiction', function($resource) {
//     return $resource('http://localhost:5000/api/v1/juridiction/:id', {id: '@id'}, {
//         get: { method: 'GET' }
//     });
// })
// .factory('Style', function($resource) {
//     return $resource('http://localhost:5000/api/v1/juridiction', {}, {
//         query: { method: 'GET', isArray: true}
//     });
// })
.factory('Search', function($resource) {
    return $resource('http://localhost:5000/api/v1/search', {q: '@q'}, {
        query: { method: 'GET', isArray: true}
    });
});

myApp.config(function($routeProvider) {
    $routeProvider
    .when('/', {
        templateUrl: 'pages/main.html',
        controller: 'mainController'
    })
    .when('/newWork', {
        templateUrl: 'pages/work_new.html',
        controller: 'newWorkController'
    })
    .when('/works', {
        templateUrl: 'pages/works.html',
        controller: 'workListController'
    })
    .when('/works/:id', {
        templateUrl: 'pages/work_details.html',
        controller: 'workDetailsController'
    })
});

// myApp.filter('filterJuridiction', function() {
//   return function(input) {
//     var output = new Array();
//     for (i=0; i<input.length; i++) {
//         if (input[i].checked == true) {
//             output.push(input[i].report);
//         }
//     }
//     return output;
//   }
// });

myApp.controller(
    'mainController',
    function ($scope, Search) {
        $scope.search = function() {
            q = $scope.searchString;
            if (q.length > 1) {
                $scope.results = Search.query({q: q});
            }
        };
    }
);

// myApp.controller(
//     'newWorkController',
//     function ($scope, Juridiction, Works, $location, $timeout, $filter) {
//         $scope.juridiction = Juridiction.query();
//         $scope.insertWork = function () {
//             $scope.work.juridiction = $filter('filterJuridiction')($scope.juridiction);
//             Works.create($scope.work);
//             $timeout(function (){
//                 $location.path('/works').search({'created': $scope.work.report});
//             }, 500);
//         };
//         $scope.cancel = function() {
//             $location.path('/works');
//         };
//     }
//
// );

// myApp.controller(
//     'workListController',
//     function ($scope, Works, Work, $location, $timeout) {
//         if ($location.search().hasOwnProperty('created')) {
//             $scope.created = $location.search()['created'];
//         }
//         if ($location.search().hasOwnProperty('deleted')) {
//             $scope.deleted = $location.search()['deleted'];
//         }
//         $scope.deleteWork = function(work_id) {
//             var deleted = Work.delete({id: work_id});
//             $timeout(function(){
//                 $location.path('/works').search({'deleted': 1})
//             }, 500);
//             //$scope.works = Works.query();
//         };
//         $scope.works = Works.query();
//     }
// );
//
// myApp.controller(
//     'workDetailsController', ['$scope', 'Work', '$routeParams',
//     function ($scope, Work, $routeParams) {
//         $scope.work = Work.get({id: $routeParams.id});
//     }
// ]);
