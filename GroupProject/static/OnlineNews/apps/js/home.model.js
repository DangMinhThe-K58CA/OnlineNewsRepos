var app = angular.module("homeApp", []).config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
});
app.controller("categoryController", function($scope) {
	$scope.categoriesList = []
	$scope.init = function () {
		$.ajax({
			url: "/getCategories",
			type: "GET",
			success: function (jsonData) {
				$scope.categoriesList = JSON.parse(jsonData);
				for (var i = 0; i < $scope.categoriesList.length; i ++) {
					var idTmp = $scope.categoriesList[i]["pk"];
					$scope.categoriesList[i] = $scope.categoriesList[i]["fields"];
					$scope.categoriesList[i].id = idTmp;
				}
				$scope.$apply();
			}
		});
	}	
	$scope.loadCategory = function(cateId) {
		alert(cateId);
	}
});


app.controller("hottestNewsController", function($scope) {
	$scope.hottestList = [];
	$scope.init = function() {
		$.ajax({
			url: "/getHottestList",
			type: "GET",
			success: function(jsonData) {
				$scope.hottestList = JSON.parse(jsonData);
				for(var i = 0; i < $scope.hottestList.length; i ++) {
					var idTmp = $scope.hottestList[i]["pk"];
					$scope.hottestList[i] = $scope.hottestList[i]["fields"];
					$scope.hottestList[i].id = idTmp;
					$scope.hottestList[i].order = i + 1;
				}
				$scope.$apply();
			}
		});
	}
	$scope.loadNews = function(newsId) {
		alert(newsId);
	}
});