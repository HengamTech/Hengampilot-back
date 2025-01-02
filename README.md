# Persian Trustpilot - Overview

This platform is a Persian version of Trustpilot designed for the Iranian market. The goal of this platform is to provide an environment for users to leave reviews and ratings for various businesses in Iran. Users can rate and review businesses they have experienced, and businesses can create their profiles to gather customer feedback to improve their services and products.

## Key Features

- **Search and View Businesses by Categories**: Users can search for businesses based on different categories and view their ratings and reviews.
  
- **Add and Manage Reviews and Ratings**: Users can add reviews and rate businesses they've interacted with.
  
- **User Registration and Login System**: Users can register and log in to manage their profiles, reviews, and ratings.
  
- **Business Profile Management**: Businesses can create and manage their profiles to showcase their information and respond to customer reviews.
  
- **Subscription System for Additional Features**: Users and businesses can access additional features through various subscription plans.
  
## Purpose

The platform allows customers to share their experiences with businesses in Iran, helping other users make informed decisions and providing businesses with valuable feedback for improvement.

---

## Technologies Used

- Django (for backend)
- Django Rest Framework (for API)
- PostgreSQL (for database)
- React.js (for frontend, if applicable)
- Docker (optional for containerization)

---

## Usage

To use the platform:

1. Register and create a user profile.
2. Search for businesses by categories.
3. Rate businesses and leave reviews.
4. Businesses can create a profile to manage their information and responses to reviews.

---

## API Endpoints

For detailed API endpoints, please refer to the full [API Documentation](./api_documentation.md).

---




# API Documentation

Welcome to the API documentation for Hengam Pilot.

## Authentication

This API uses JWT for authentication. Please provide the token in the `Authorization` header as `Bearer <token>` for all requests.

## Endpoints



# API Documentation

> Version 1.2.1

Hengam pilot

## Path Table

| Method | Path | Description |
| --- | --- | --- |
| GET | [/analytics/audit-logs/](#getanalyticsaudit-logs) |  |
| GET | [/analytics/audit-logs/{id}/](#getanalyticsaudit-logsid) |  |
| GET | [/api/schema/](#getapischema) |  |
| POST | [/api/token/](#postapitoken) |  |
| POST | [/api/token/refresh/](#postapitokenrefresh) |  |
| GET | [/business_management/businesses/](#getbusiness_managementbusinesses) |  |
| POST | [/business_management/businesses/](#postbusiness_managementbusinesses) |  |
| GET | [/business_management/businesses/{id}/](#getbusiness_managementbusinessesid) |  |
| PUT | [/business_management/businesses/{id}/](#putbusiness_managementbusinessesid) |  |
| PATCH | [/business_management/businesses/{id}/](#patchbusiness_managementbusinessesid) |  |
| DELETE | [/business_management/businesses/{id}/](#deletebusiness_managementbusinessesid) |  |
| GET | [/business_management/businesses/categories/](#getbusiness_managementbusinessescategories) |  |
| GET | [/business_management/businesses/category-businesses/](#getbusiness_managementbusinessescategory-businesses) |  |
| GET | [/business_management/businesses/reviews/](#getbusiness_managementbusinessesreviews) |  |
| GET | [/business_management/category/](#getbusiness_managementcategory) |  |
| POST | [/business_management/category/](#postbusiness_managementcategory) |  |
| GET | [/business_management/category/{id}/](#getbusiness_managementcategoryid) |  |
| PUT | [/business_management/category/{id}/](#putbusiness_managementcategoryid) |  |
| PATCH | [/business_management/category/{id}/](#patchbusiness_managementcategoryid) |  |
| DELETE | [/business_management/category/{id}/](#deletebusiness_managementcategoryid) |  |
| GET | [/business_management/subscription/](#getbusiness_managementsubscription) |  |
| POST | [/business_management/subscription/](#postbusiness_managementsubscription) |  |
| GET | [/business_management/subscription/{id}/](#getbusiness_managementsubscriptionid) |  |
| PUT | [/business_management/subscription/{id}/](#putbusiness_managementsubscriptionid) |  |
| PATCH | [/business_management/subscription/{id}/](#patchbusiness_managementsubscriptionid) |  |
| DELETE | [/business_management/subscription/{id}/](#deletebusiness_managementsubscriptionid) |  |
| POST | [/business_management/subscription/{id}/manage/](#postbusiness_managementsubscriptionidmanage) |  |
| GET | [/platform/feature-requests/](#getplatformfeature-requests) |  |
| POST | [/platform/feature-requests/](#postplatformfeature-requests) |  |
| GET | [/platform/feature-requests/{id}/](#getplatformfeature-requestsid) |  |
| PUT | [/platform/feature-requests/{id}/](#putplatformfeature-requestsid) |  |
| PATCH | [/platform/feature-requests/{id}/](#patchplatformfeature-requestsid) |  |
| DELETE | [/platform/feature-requests/{id}/](#deleteplatformfeature-requestsid) |  |
| GET | [/review_rating/reports/](#getreview_ratingreports) |  |
| POST | [/review_rating/reports/](#postreview_ratingreports) |  |
| GET | [/review_rating/reports/{id}/](#getreview_ratingreportsid) |  |
| PUT | [/review_rating/reports/{id}/](#putreview_ratingreportsid) |  |
| PATCH | [/review_rating/reports/{id}/](#patchreview_ratingreportsid) |  |
| DELETE | [/review_rating/reports/{id}/](#deletereview_ratingreportsid) |  |
| POST | [/review_rating/reports/add_report/](#postreview_ratingreportsadd_report) |  |
| GET | [/review_rating/review_responses/](#getreview_ratingreview_responses) |  |
| POST | [/review_rating/review_responses/](#postreview_ratingreview_responses) |  |
| GET | [/review_rating/review_responses/{id}/](#getreview_ratingreview_responsesid) |  |
| PUT | [/review_rating/review_responses/{id}/](#putreview_ratingreview_responsesid) |  |
| PATCH | [/review_rating/review_responses/{id}/](#patchreview_ratingreview_responsesid) |  |
| DELETE | [/review_rating/review_responses/{id}/](#deletereview_ratingreview_responsesid) |  |
| GET | [/review_rating/reviews/](#getreview_ratingreviews) |  |
| POST | [/review_rating/reviews/](#postreview_ratingreviews) |  |
| GET | [/review_rating/reviews/{id}/](#getreview_ratingreviewsid) |  |
| PUT | [/review_rating/reviews/{id}/](#putreview_ratingreviewsid) |  |
| PATCH | [/review_rating/reviews/{id}/](#patchreview_ratingreviewsid) |  |
| DELETE | [/review_rating/reviews/{id}/](#deletereview_ratingreviewsid) |  |
| POST | [/review_rating/reviews/add_review/](#postreview_ratingreviewsadd_review) |  |
| GET | [/review_rating/reviews/average-rating/](#getreview_ratingreviewsaverage-rating) |  |
| GET | [/review_rating/reviews/count-all-reviews/](#getreview_ratingreviewscount-all-reviews) |  |
| GET | [/review_rating/reviews/count-unapproved-reviews/](#getreview_ratingreviewscount-unapproved-reviews) |  |
| GET | [/review_rating/reviews/reviews-by-user/](#getreview_ratingreviewsreviews-by-user) |  |
| GET | [/review_rating/reviews/view_reviews/](#getreview_ratingreviewsview_reviews) |  |
| GET | [/review_rating/reviews/waiting-approval-reviews/](#getreview_ratingreviewswaiting-approval-reviews) |  |
| GET | [/review_rating/votes/](#getreview_ratingvotes) |  |
| POST | [/review_rating/votes/](#postreview_ratingvotes) |  |
| GET | [/review_rating/votes/{id}/](#getreview_ratingvotesid) |  |
| PUT | [/review_rating/votes/{id}/](#putreview_ratingvotesid) |  |
| PATCH | [/review_rating/votes/{id}/](#patchreview_ratingvotesid) |  |
| DELETE | [/review_rating/votes/{id}/](#deletereview_ratingvotesid) |  |
| GET | [/review_rating/votes/reviews-liked-by-user/](#getreview_ratingvotesreviews-liked-by-user) |  |
| GET | [/user_management/notifications/](#getuser_managementnotifications) |  |
| POST | [/user_management/notifications/](#postuser_managementnotifications) |  |
| GET | [/user_management/notifications/{id}/](#getuser_managementnotificationsid) |  |
| PUT | [/user_management/notifications/{id}/](#putuser_managementnotificationsid) |  |
| PATCH | [/user_management/notifications/{id}/](#patchuser_managementnotificationsid) |  |
| DELETE | [/user_management/notifications/{id}/](#deleteuser_managementnotificationsid) |  |
| GET | [/user_management/users/](#getuser_managementusers) |  |
| POST | [/user_management/users/](#postuser_managementusers) |  |
| GET | [/user_management/users/{id}/](#getuser_managementusersid) |  |
| PUT | [/user_management/users/{id}/](#putuser_managementusersid) |  |
| PATCH | [/user_management/users/{id}/](#patchuser_managementusersid) |  |
| DELETE | [/user_management/users/{id}/](#deleteuser_managementusersid) |  |
| POST | [/user_management/users/{id}/update-password/](#postuser_managementusersidupdate-password) |  |
| GET | [/user_management/users/active-users/](#getuser_managementusersactive-users) |  |
| GET | [/user_management/users/fetch-by-username/](#getuser_managementusersfetch-by-username) |  |
| GET | [/user_management/users/inactive-users/](#getuser_managementusersinactive-users) |  |
| GET | [/user_management/users/me/](#getuser_managementusersme) |  |
| GET | [/user_management/users/total-users/](#getuser_managementuserstotal-users) |  |
| GET | [/user_management/users/user-review-count/](#getuser_managementusersuser-review-count) |  |

## Reference Table

| Name | Path | Description |
| --- | --- | --- |
| AuditLog | [#/components/schemas/AuditLog](#componentsschemasauditlog) |  |
| Business | [#/components/schemas/Business](#componentsschemasbusiness) |  |
| BusinessCreate | [#/components/schemas/BusinessCreate](#componentsschemasbusinesscreate) |  |
| BusinessUpdate | [#/components/schemas/BusinessUpdate](#componentsschemasbusinessupdate) |  |
| Category | [#/components/schemas/Category](#componentsschemascategory) |  |
| FeatureRequest | [#/components/schemas/FeatureRequest](#componentsschemasfeaturerequest) |  |
| Notification | [#/components/schemas/Notification](#componentsschemasnotification) |  |
| PatchedBusinessUpdate | [#/components/schemas/PatchedBusinessUpdate](#componentsschemaspatchedbusinessupdate) |  |
| PatchedCategory | [#/components/schemas/PatchedCategory](#componentsschemaspatchedcategory) |  |
| PatchedFeatureRequest | [#/components/schemas/PatchedFeatureRequest](#componentsschemaspatchedfeaturerequest) |  |
| PatchedNotification | [#/components/schemas/PatchedNotification](#componentsschemaspatchednotification) |  |
| PatchedReports | [#/components/schemas/PatchedReports](#componentsschemaspatchedreports) |  |
| PatchedReview | [#/components/schemas/PatchedReview](#componentsschemaspatchedreview) |  |
| PatchedReviewResponse | [#/components/schemas/PatchedReviewResponse](#componentsschemaspatchedreviewresponse) |  |
| PatchedSubscription | [#/components/schemas/PatchedSubscription](#componentsschemaspatchedsubscription) |  |
| PatchedUser | [#/components/schemas/PatchedUser](#componentsschemaspatcheduser) |  |
| PatchedVote | [#/components/schemas/PatchedVote](#componentsschemaspatchedvote) |  |
| RankEnum | [#/components/schemas/RankEnum](#componentsschemasrankenum) | * `1` - Very Poor
* `2` - Poor
* `3` - Medium
* `4` - Good
* `5` - Very Good |
| ReasonSelectEnum | [#/components/schemas/ReasonSelectEnum](#componentsschemasreasonselectenum) | * `sexual` - SEXUAL
* `violence` - VIOLENCE
* `accusations` - ACCUSATIONS
* `terrorism` - TERRORISM |
| Reports | [#/components/schemas/Reports](#componentsschemasreports) |  |
| ResultReportEnum | [#/components/schemas/ResultReportEnum](#componentsschemasresultreportenum) | * `ignore` - Ignore
* `Unchecked` - Unchecked
* `Remove` - Remove
* `UserBan` - User_Ban |
| Review | [#/components/schemas/Review](#componentsschemasreview) |  |
| ReviewResponse | [#/components/schemas/ReviewResponse](#componentsschemasreviewresponse) |  |
| StatusEnum | [#/components/schemas/StatusEnum](#componentsschemasstatusenum) | * `pending` - PENDING
* `approved` - APPROVED
* `rejected` - REJECTED |
| Subscription | [#/components/schemas/Subscription](#componentsschemassubscription) |  |
| TokenObtainPair | [#/components/schemas/TokenObtainPair](#componentsschemastokenobtainpair) |  |
| TokenRefresh | [#/components/schemas/TokenRefresh](#componentsschemastokenrefresh) |  |
| TypeEnum | [#/components/schemas/TypeEnum](#componentsschemastypeenum) | * `free` - FREE
* `premium` - PREMIUM |
| User | [#/components/schemas/User](#componentsschemasuser) |  |
| Vote | [#/components/schemas/Vote](#componentsschemasvote) |  |
| jwtAuth | [#/components/securitySchemes/jwtAuth](#componentssecurityschemesjwtauth) |  |

## Path Details

***

### [GET]/analytics/audit-logs/

- Security  
jwtAuth  

#### Parameters(Query)

```ts
action_type?: string
```

```ts
content_type?: integer
```

```ts
search?: string
```

```ts
user?: string
```

#### Responses

- 200 

`application/json`

```ts
{
  id: string
  content_type: string
  user: string
  action_time: string
  action_type: string
  object_id: string
  changes?: string
  ip_address?: string
  user_agent?: string
}[]
```

***

### [GET]/analytics/audit-logs/{id}/

- Security  
jwtAuth  

#### Responses

- 200 

`application/json`

```ts
{
  id: string
  content_type: string
  user: string
  action_time: string
  action_type: string
  object_id: string
  changes?: string
  ip_address?: string
  user_agent?: string
}
```

***

### [GET]/api/schema/

- Description  
OpenApi3 schema for this API. Format can be selected via content negotiation.  
  
- YAML: application/vnd.oai.openapi  
- JSON: application/vnd.oai.openapi+json

- Security  
jwtAuth  
undefined  

#### Parameters(Query)

```ts
format?: enum[json, yaml]
```

```ts
lang?: enum[af, ar, ar-dz, ast, az, be, bg, bn, br, bs, ca, ckb, cs, cy, da, de, dsb, el, en, en-au, en-gb, eo, es, es-ar, es-co, es-mx, es-ni, es-ve, et, eu, fa, fi, fr, fy, ga, gd, gl, he, hi, hr, hsb, hu, hy, ia, id, ig, io, is, it, ja, ka, kab, kk, km, kn, ko, ky, lb, lt, lv, mk, ml, mn, mr, ms, my, nb, ne, nl, nn, os, pa, pl, pt, pt-br, ro, ru, sk, sl, sq, sr, sr-latn, sv, sw, ta, te, tg, th, tk, tr, tt, udm, uk, ur, uz, vi, zh-hans, zh-hant]
```

#### Responses

- 200 

`application/vnd.oai.openapi`

```ts
{
}
```

`application/yaml`

```ts
{
}
```

`application/vnd.oai.openapi+json`

```ts
{
}
```

`application/json`

```ts
{
}
```

***

### [POST]/api/token/

- Description  
Takes a set of user credentials and returns an access and refresh JSON web  
token pair to prove the authentication of those credentials.

#### RequestBody

- application/json

```ts
{
  username: string
  password: string
  access: string
  refresh: string
}
```

- application/x-www-form-urlencoded

```ts
{
  username: string
  password: string
  access: string
  refresh: string
}
```

- multipart/form-data

```ts
{
  username: string
  password: string
  access: string
  refresh: string
}
```

#### Responses

- 200 

`application/json`

```ts
{
  username: string
  password: string
  access: string
  refresh: string
}
```

***

### [POST]/api/token/refresh/

- Description  
Takes a refresh type JSON web token and returns an access type JSON web  
token if the refresh token is valid.

#### RequestBody

- application/json

```ts
{
  access: string
  refresh: string
}
```

- application/x-www-form-urlencoded

```ts
{
  access: string
  refresh: string
}
```

- multipart/form-data

```ts
{
  access: string
  refresh: string
}
```

#### Responses

- 200 

`application/json`

```ts
{
  access: string
  refresh: string
}
```

***

### [GET]/business_management/businesses/

- Security  
jwtAuth  
undefined  

#### Parameters(Query)

```ts
ordering?: string
```

```ts
search?: string
```

#### Responses

- 200 

`application/json`

```ts
{
  id: string
  average_rating: string
  total_reviews: string
  business_image_url: string
  business_image?: string
  business_name: string
  description: string
  website_url?: string
  average_rank: integer
  created_at: string
  updated_at: string
  business_category?: string
  business_owner: string
}[]
```

***

### [POST]/business_management/businesses/

- Security  
jwtAuth  

#### RequestBody

- application/json

```ts
{
  business_image?: string
  business_owner: string
  business_name: string
  description: string
  website_url?: string
  business_category?: string
}
```

- application/x-www-form-urlencoded

```ts
{
  business_image?: string
  business_owner: string
  business_name: string
  description: string
  website_url?: string
  business_category?: string
}
```

- multipart/form-data

```ts
{
  business_image?: string
  business_owner: string
  business_name: string
  description: string
  website_url?: string
  business_category?: string
}
```

#### Responses

- 201 

`application/json`

```ts
{
  business_image?: string
  business_owner: string
  business_name: string
  description: string
  website_url?: string
  business_category?: string
}
```

***

### [GET]/business_management/businesses/{id}/

- Security  
jwtAuth  
undefined  

#### Responses

- 200 

`application/json`

```ts
{
  id: string
  average_rating: string
  total_reviews: string
  business_image_url: string
  business_image?: string
  business_name: string
  description: string
  website_url?: string
  average_rank: integer
  created_at: string
  updated_at: string
  business_category?: string
  business_owner: string
}
```

***

### [PUT]/business_management/businesses/{id}/

- Security  
jwtAuth  

#### RequestBody

- application/json

```ts
{
  business_image?: string
  business_owner: string
  business_name: string
  description: string
  website_url?: string
}
```

- application/x-www-form-urlencoded

```ts
{
  business_image?: string
  business_owner: string
  business_name: string
  description: string
  website_url?: string
}
```

- multipart/form-data

```ts
{
  business_image?: string
  business_owner: string
  business_name: string
  description: string
  website_url?: string
}
```

#### Responses

- 200 

`application/json`

```ts
{
  business_image?: string
  business_owner: string
  business_name: string
  description: string
  website_url?: string
}
```

***

### [PATCH]/business_management/businesses/{id}/

- Security  
jwtAuth  

#### RequestBody

- application/json

```ts
{
  business_image?: string
  business_owner?: string
  business_name?: string
  description?: string
  website_url?: string
}
```

- application/x-www-form-urlencoded

```ts
{
  business_image?: string
  business_owner?: string
  business_name?: string
  description?: string
  website_url?: string
}
```

- multipart/form-data

```ts
{
  business_image?: string
  business_owner?: string
  business_name?: string
  description?: string
  website_url?: string
}
```

#### Responses

- 200 

`application/json`

```ts
{
  business_image?: string
  business_owner: string
  business_name: string
  description: string
  website_url?: string
}
```

***

### [DELETE]/business_management/businesses/{id}/

- Security  
jwtAuth  

#### Responses

- 204 No response body

***

### [GET]/business_management/businesses/categories/

- Security  
jwtAuth  

#### Responses

- 200 

`application/json`

```ts
{
  id: string
  average_rating: string
  total_reviews: string
  business_image_url: string
  business_image?: string
  business_name: string
  description: string
  website_url?: string
  average_rank: integer
  created_at: string
  updated_at: string
  business_category?: string
  business_owner: string
}
```

***

### [GET]/business_management/businesses/category-businesses/

- Security  
jwtAuth  

#### Parameters(Query)

```ts
category_name?: string
```

#### Responses

- 200 

`application/json`

```ts
// Unspecified response body
{
}
```

- 400 

`application/json`

```ts
// Unspecified response body
{
}
```

- 404 

`application/json`

```ts
// Unspecified response body
{
}
```

***

### [GET]/business_management/businesses/reviews/

- Security  
jwtAuth  

#### Parameters(Query)

```ts
id?: string
```

```ts
name?: string
```

```ts
ordering?: string
```

```ts
search?: string
```

#### Responses

- 200 

`application/json`

```ts
{
  id: string
  rank?: #/components/schemas/RankEnum
  review_text: string
  hidden?: boolean
  created_at: string
  updated_at: string
  user: string
  business_id: string
}[]
```

- 400 

`application/json`

```ts
// Unspecified response body
{
}
```

- 404 

`application/json`

```ts
// Unspecified response body
{
}
```

***

### [GET]/business_management/category/

- Security  
jwtAuth  
undefined  

#### Parameters(Query)

```ts
ordering?: string
```

```ts
search?: string
```

#### Responses

- 200 

`application/json`

```ts
{
  id: string
  category_name: string
  category_image?: string
}[]
```

***

### [POST]/business_management/category/

- Security  
jwtAuth  

#### RequestBody

- application/json

```ts
{
  id: string
  category_name: string
  category_image?: string
}
```

- application/x-www-form-urlencoded

```ts
{
  id: string
  category_name: string
  category_image?: string
}
```

- multipart/form-data

```ts
{
  id: string
  category_name: string
  category_image?: string
}
```

#### Responses

- 201 

`application/json`

```ts
{
  id: string
  category_name: string
  category_image?: string
}
```

***

### [GET]/business_management/category/{id}/

- Security  
jwtAuth  
undefined  

#### Responses

- 200 

`application/json`

```ts
{
  id: string
  category_name: string
  category_image?: string
}
```

***

### [PUT]/business_management/category/{id}/

- Security  
jwtAuth  

#### RequestBody

- application/json

```ts
{
  id: string
  category_name: string
  category_image?: string
}
```

- application/x-www-form-urlencoded

```ts
{
  id: string
  category_name: string
  category_image?: string
}
```

- multipart/form-data

```ts
{
  id: string
  category_name: string
  category_image?: string
}
```

#### Responses

- 200 

`application/json`

```ts
{
  id: string
  category_name: string
  category_image?: string
}
```

***

### [PATCH]/business_management/category/{id}/

- Security  
jwtAuth  

#### RequestBody

- application/json

```ts
{
  id?: string
  category_name?: string
  category_image?: string
}
```

- application/x-www-form-urlencoded

```ts
{
  id?: string
  category_name?: string
  category_image?: string
}
```

- multipart/form-data

```ts
{
  id?: string
  category_name?: string
  category_image?: string
}
```

#### Responses

- 200 

`application/json`

```ts
{
  id: string
  category_name: string
  category_image?: string
}
```

***

### [DELETE]/business_management/category/{id}/

- Security  
jwtAuth  

#### Responses

- 204 No response body

***

### [GET]/business_management/subscription/

- Security  
jwtAuth  

#### Parameters(Query)

```ts
ordering?: string
```

```ts
search?: string
```

#### Responses

- 200 

`application/json`

```ts
{
  id: string
  // * `free` - FREE
  // * `premium` - PREMIUM
  type?: enum[free, premium]
  start_date: string
  end_date: string
  is_active?: boolean
  business: string
}[]
```

***

### [POST]/business_management/subscription/

- Security  
jwtAuth  

#### RequestBody

- application/json

```ts
{
  id: string
  // * `free` - FREE
  // * `premium` - PREMIUM
  type?: enum[free, premium]
  start_date: string
  end_date: string
  is_active?: boolean
  business: string
}
```

- application/x-www-form-urlencoded

```ts
{
  id: string
  // * `free` - FREE
  // * `premium` - PREMIUM
  type?: enum[free, premium]
  start_date: string
  end_date: string
  is_active?: boolean
  business: string
}
```

- multipart/form-data

```ts
{
  id: string
  // * `free` - FREE
  // * `premium` - PREMIUM
  type?: enum[free, premium]
  start_date: string
  end_date: string
  is_active?: boolean
  business: string
}
```

#### Responses

- 201 

`application/json`

```ts
{
  id: string
  // * `free` - FREE
  // * `premium` - PREMIUM
  type?: enum[free, premium]
  start_date: string
  end_date: string
  is_active?: boolean
  business: string
}
```

***

### [GET]/business_management/subscription/{id}/

- Security  
jwtAuth  

#### Responses

- 200 

`application/json`

```ts
{
  id: string
  // * `free` - FREE
  // * `premium` - PREMIUM
  type?: enum[free, premium]
  start_date: string
  end_date: string
  is_active?: boolean
  business: string
}
```

***

### [PUT]/business_management/subscription/{id}/

- Security  
jwtAuth  

#### RequestBody

- application/json

```ts
{
  id: string
  // * `free` - FREE
  // * `premium` - PREMIUM
  type?: enum[free, premium]
  start_date: string
  end_date: string
  is_active?: boolean
  business: string
}
```

- application/x-www-form-urlencoded

```ts
{
  id: string
  // * `free` - FREE
  // * `premium` - PREMIUM
  type?: enum[free, premium]
  start_date: string
  end_date: string
  is_active?: boolean
  business: string
}
```

- multipart/form-data

```ts
{
  id: string
  // * `free` - FREE
  // * `premium` - PREMIUM
  type?: enum[free, premium]
  start_date: string
  end_date: string
  is_active?: boolean
  business: string
}
```

#### Responses

- 200 

`application/json`

```ts
{
  id: string
  // * `free` - FREE
  // * `premium` - PREMIUM
  type?: enum[free, premium]
  start_date: string
  end_date: string
  is_active?: boolean
  business: string
}
```

***

### [PATCH]/business_management/subscription/{id}/

- Security  
jwtAuth  

#### RequestBody

- application/json

```ts
{
  id?: string
  // * `free` - FREE
  // * `premium` - PREMIUM
  type?: enum[free, premium]
  start_date?: string
  end_date?: string
  is_active?: boolean
  business?: string
}
```

- application/x-www-form-urlencoded

```ts
{
  id?: string
  // * `free` - FREE
  // * `premium` - PREMIUM
  type?: enum[free, premium]
  start_date?: string
  end_date?: string
  is_active?: boolean
  business?: string
}
```

- multipart/form-data

```ts
{
  id?: string
  // * `free` - FREE
  // * `premium` - PREMIUM
  type?: enum[free, premium]
  start_date?: string
  end_date?: string
  is_active?: boolean
  business?: string
}
```

#### Responses

- 200 

`application/json`

```ts
{
  id: string
  // * `free` - FREE
  // * `premium` - PREMIUM
  type?: enum[free, premium]
  start_date: string
  end_date: string
  is_active?: boolean
  business: string
}
```

***

### [DELETE]/business_management/subscription/{id}/

- Security  
jwtAuth  

#### Responses

- 204 No response body

***

### [POST]/business_management/subscription/{id}/manage/

- Security  
jwtAuth  

#### RequestBody

- application/json

```ts
{
  id: string
  // * `free` - FREE
  // * `premium` - PREMIUM
  type?: enum[free, premium]
  start_date: string
  end_date: string
  is_active?: boolean
  business: string
}
```

- application/x-www-form-urlencoded

```ts
{
  id: string
  // * `free` - FREE
  // * `premium` - PREMIUM
  type?: enum[free, premium]
  start_date: string
  end_date: string
  is_active?: boolean
  business: string
}
```

- multipart/form-data

```ts
{
  id: string
  // * `free` - FREE
  // * `premium` - PREMIUM
  type?: enum[free, premium]
  start_date: string
  end_date: string
  is_active?: boolean
  business: string
}
```

#### Responses

- 200 

`application/json`

```ts
{
  id: string
  // * `free` - FREE
  // * `premium` - PREMIUM
  type?: enum[free, premium]
  start_date: string
  end_date: string
  is_active?: boolean
  business: string
}
```

***

### [GET]/platform/feature-requests/

- Security  
jwtAuth  

#### Parameters(Query)

```ts
ordering?: string
```

```ts
search?: string
```

#### Responses

- 200 

`application/json`

```ts
{
  id: string
  description: string
  // * `pending` - PENDING
  // * `approved` - APPROVED
  // * `rejected` - REJECTED
  status?: enum[pending, approved, rejected]
  user: string
}[]
```

***

### [POST]/platform/feature-requests/

- Security  
jwtAuth  

#### RequestBody

- application/json

```ts
{
  id: string
  description: string
  // * `pending` - PENDING
  // * `approved` - APPROVED
  // * `rejected` - REJECTED
  status?: enum[pending, approved, rejected]
  user: string
}
```

- application/x-www-form-urlencoded

```ts
{
  id: string
  description: string
  // * `pending` - PENDING
  // * `approved` - APPROVED
  // * `rejected` - REJECTED
  status?: enum[pending, approved, rejected]
  user: string
}
```

- multipart/form-data

```ts
{
  id: string
  description: string
  // * `pending` - PENDING
  // * `approved` - APPROVED
  // * `rejected` - REJECTED
  status?: enum[pending, approved, rejected]
  user: string
}
```

#### Responses

- 201 

`application/json`

```ts
{
  id: string
  description: string
  // * `pending` - PENDING
  // * `approved` - APPROVED
  // * `rejected` - REJECTED
  status?: enum[pending, approved, rejected]
  user: string
}
```

***

### [GET]/platform/feature-requests/{id}/

- Security  
jwtAuth  

#### Responses

- 200 

`application/json`

```ts
{
  id: string
  description: string
  // * `pending` - PENDING
  // * `approved` - APPROVED
  // * `rejected` - REJECTED
  status?: enum[pending, approved, rejected]
  user: string
}
```

***

### [PUT]/platform/feature-requests/{id}/

- Security  
jwtAuth  

#### RequestBody

- application/json

```ts
{
  id: string
  description: string
  // * `pending` - PENDING
  // * `approved` - APPROVED
  // * `rejected` - REJECTED
  status?: enum[pending, approved, rejected]
  user: string
}
```

- application/x-www-form-urlencoded

```ts
{
  id: string
  description: string
  // * `pending` - PENDING
  // * `approved` - APPROVED
  // * `rejected` - REJECTED
  status?: enum[pending, approved, rejected]
  user: string
}
```

- multipart/form-data

```ts
{
  id: string
  description: string
  // * `pending` - PENDING
  // * `approved` - APPROVED
  // * `rejected` - REJECTED
  status?: enum[pending, approved, rejected]
  user: string
}
```

#### Responses

- 200 

`application/json`

```ts
{
  id: string
  description: string
  // * `pending` - PENDING
  // * `approved` - APPROVED
  // * `rejected` - REJECTED
  status?: enum[pending, approved, rejected]
  user: string
}
```

***

### [PATCH]/platform/feature-requests/{id}/

- Security  
jwtAuth  

#### RequestBody

- application/json

```ts
{
  id?: string
  description?: string
  // * `pending` - PENDING
  // * `approved` - APPROVED
  // * `rejected` - REJECTED
  status?: enum[pending, approved, rejected]
  user?: string
}
```

- application/x-www-form-urlencoded

```ts
{
  id?: string
  description?: string
  // * `pending` - PENDING
  // * `approved` - APPROVED
  // * `rejected` - REJECTED
  status?: enum[pending, approved, rejected]
  user?: string
}
```

- multipart/form-data

```ts
{
  id?: string
  description?: string
  // * `pending` - PENDING
  // * `approved` - APPROVED
  // * `rejected` - REJECTED
  status?: enum[pending, approved, rejected]
  user?: string
}
```

#### Responses

- 200 

`application/json`

```ts
{
  id: string
  description: string
  // * `pending` - PENDING
  // * `approved` - APPROVED
  // * `rejected` - REJECTED
  status?: enum[pending, approved, rejected]
  user: string
}
```

***

### [DELETE]/platform/feature-requests/{id}/

- Security  
jwtAuth  

#### Responses

- 204 No response body

***

### [GET]/review_rating/reports/

- Security  
jwtAuth  

#### Parameters(Query)

```ts
ordering?: string
```

```ts
search?: string
```

#### Responses

- 200 

`application/json`

```ts
{
  id: string
  // * `sexual` - SEXUAL
  // * `violence` - VIOLENCE
  // * `accusations` - ACCUSATIONS
  // * `terrorism` - TERRORISM
  reason_select: enum[sexual, violence, accusations, terrorism]
  // * `ignore` - Ignore
  // * `Unchecked` - Unchecked
  // * `Remove` - Remove
  // * `UserBan` - User_Ban
  result_report?: enum[ignore, Unchecked, Remove, UserBan]
  reason: string
  create_at: string
  review_id: string
  review_user_id: string
}[]
```

***

### [POST]/review_rating/reports/

- Security  
jwtAuth  

#### RequestBody

- application/json

```ts
{
  id: string
  // * `sexual` - SEXUAL
  // * `violence` - VIOLENCE
  // * `accusations` - ACCUSATIONS
  // * `terrorism` - TERRORISM
  reason_select: enum[sexual, violence, accusations, terrorism]
  // * `ignore` - Ignore
  // * `Unchecked` - Unchecked
  // * `Remove` - Remove
  // * `UserBan` - User_Ban
  result_report?: enum[ignore, Unchecked, Remove, UserBan]
  reason: string
  create_at: string
  review_id: string
  review_user_id: string
}
```

- application/x-www-form-urlencoded

```ts
{
  id: string
  // * `sexual` - SEXUAL
  // * `violence` - VIOLENCE
  // * `accusations` - ACCUSATIONS
  // * `terrorism` - TERRORISM
  reason_select: enum[sexual, violence, accusations, terrorism]
  // * `ignore` - Ignore
  // * `Unchecked` - Unchecked
  // * `Remove` - Remove
  // * `UserBan` - User_Ban
  result_report?: enum[ignore, Unchecked, Remove, UserBan]
  reason: string
  create_at: string
  review_id: string
  review_user_id: string
}
```

- multipart/form-data

```ts
{
  id: string
  // * `sexual` - SEXUAL
  // * `violence` - VIOLENCE
  // * `accusations` - ACCUSATIONS
  // * `terrorism` - TERRORISM
  reason_select: enum[sexual, violence, accusations, terrorism]
  // * `ignore` - Ignore
  // * `Unchecked` - Unchecked
  // * `Remove` - Remove
  // * `UserBan` - User_Ban
  result_report?: enum[ignore, Unchecked, Remove, UserBan]
  reason: string
  create_at: string
  review_id: string
  review_user_id: string
}
```

#### Responses

- 201 

`application/json`

```ts
{
  id: string
  // * `sexual` - SEXUAL
  // * `violence` - VIOLENCE
  // * `accusations` - ACCUSATIONS
  // * `terrorism` - TERRORISM
  reason_select: enum[sexual, violence, accusations, terrorism]
  // * `ignore` - Ignore
  // * `Unchecked` - Unchecked
  // * `Remove` - Remove
  // * `UserBan` - User_Ban
  result_report?: enum[ignore, Unchecked, Remove, UserBan]
  reason: string
  create_at: string
  review_id: string
  review_user_id: string
}
```

***

### [GET]/review_rating/reports/{id}/

- Security  
jwtAuth  

#### Responses

- 200 

`application/json`

```ts
{
  id: string
  // * `sexual` - SEXUAL
  // * `violence` - VIOLENCE
  // * `accusations` - ACCUSATIONS
  // * `terrorism` - TERRORISM
  reason_select: enum[sexual, violence, accusations, terrorism]
  // * `ignore` - Ignore
  // * `Unchecked` - Unchecked
  // * `Remove` - Remove
  // * `UserBan` - User_Ban
  result_report?: enum[ignore, Unchecked, Remove, UserBan]
  reason: string
  create_at: string
  review_id: string
  review_user_id: string
}
```

***

### [PUT]/review_rating/reports/{id}/

- Security  
jwtAuth  

#### RequestBody

- application/json

```ts
{
  id: string
  // * `sexual` - SEXUAL
  // * `violence` - VIOLENCE
  // * `accusations` - ACCUSATIONS
  // * `terrorism` - TERRORISM
  reason_select: enum[sexual, violence, accusations, terrorism]
  // * `ignore` - Ignore
  // * `Unchecked` - Unchecked
  // * `Remove` - Remove
  // * `UserBan` - User_Ban
  result_report?: enum[ignore, Unchecked, Remove, UserBan]
  reason: string
  create_at: string
  review_id: string
  review_user_id: string
}
```

- application/x-www-form-urlencoded

```ts
{
  id: string
  // * `sexual` - SEXUAL
  // * `violence` - VIOLENCE
  // * `accusations` - ACCUSATIONS
  // * `terrorism` - TERRORISM
  reason_select: enum[sexual, violence, accusations, terrorism]
  // * `ignore` - Ignore
  // * `Unchecked` - Unchecked
  // * `Remove` - Remove
  // * `UserBan` - User_Ban
  result_report?: enum[ignore, Unchecked, Remove, UserBan]
  reason: string
  create_at: string
  review_id: string
  review_user_id: string
}
```

- multipart/form-data

```ts
{
  id: string
  // * `sexual` - SEXUAL
  // * `violence` - VIOLENCE
  // * `accusations` - ACCUSATIONS
  // * `terrorism` - TERRORISM
  reason_select: enum[sexual, violence, accusations, terrorism]
  // * `ignore` - Ignore
  // * `Unchecked` - Unchecked
  // * `Remove` - Remove
  // * `UserBan` - User_Ban
  result_report?: enum[ignore, Unchecked, Remove, UserBan]
  reason: string
  create_at: string
  review_id: string
  review_user_id: string
}
```

#### Responses

- 200 

`application/json`

```ts
{
  id: string
  // * `sexual` - SEXUAL
  // * `violence` - VIOLENCE
  // * `accusations` - ACCUSATIONS
  // * `terrorism` - TERRORISM
  reason_select: enum[sexual, violence, accusations, terrorism]
  // * `ignore` - Ignore
  // * `Unchecked` - Unchecked
  // * `Remove` - Remove
  // * `UserBan` - User_Ban
  result_report?: enum[ignore, Unchecked, Remove, UserBan]
  reason: string
  create_at: string
  review_id: string
  review_user_id: string
}
```

***

### [PATCH]/review_rating/reports/{id}/

- Security  
jwtAuth  

#### RequestBody

- application/json

```ts
{
  id?: string
  // * `sexual` - SEXUAL
  // * `violence` - VIOLENCE
  // * `accusations` - ACCUSATIONS
  // * `terrorism` - TERRORISM
  reason_select?: enum[sexual, violence, accusations, terrorism]
  // * `ignore` - Ignore
  // * `Unchecked` - Unchecked
  // * `Remove` - Remove
  // * `UserBan` - User_Ban
  result_report?: enum[ignore, Unchecked, Remove, UserBan]
  reason?: string
  create_at?: string
  review_id?: string
  review_user_id?: string
}
```

- application/x-www-form-urlencoded

```ts
{
  id?: string
  // * `sexual` - SEXUAL
  // * `violence` - VIOLENCE
  // * `accusations` - ACCUSATIONS
  // * `terrorism` - TERRORISM
  reason_select?: enum[sexual, violence, accusations, terrorism]
  // * `ignore` - Ignore
  // * `Unchecked` - Unchecked
  // * `Remove` - Remove
  // * `UserBan` - User_Ban
  result_report?: enum[ignore, Unchecked, Remove, UserBan]
  reason?: string
  create_at?: string
  review_id?: string
  review_user_id?: string
}
```

- multipart/form-data

```ts
{
  id?: string
  // * `sexual` - SEXUAL
  // * `violence` - VIOLENCE
  // * `accusations` - ACCUSATIONS
  // * `terrorism` - TERRORISM
  reason_select?: enum[sexual, violence, accusations, terrorism]
  // * `ignore` - Ignore
  // * `Unchecked` - Unchecked
  // * `Remove` - Remove
  // * `UserBan` - User_Ban
  result_report?: enum[ignore, Unchecked, Remove, UserBan]
  reason?: string
  create_at?: string
  review_id?: string
  review_user_id?: string
}
```

#### Responses

- 200 

`application/json`

```ts
{
  id: string
  // * `sexual` - SEXUAL
  // * `violence` - VIOLENCE
  // * `accusations` - ACCUSATIONS
  // * `terrorism` - TERRORISM
  reason_select: enum[sexual, violence, accusations, terrorism]
  // * `ignore` - Ignore
  // * `Unchecked` - Unchecked
  // * `Remove` - Remove
  // * `UserBan` - User_Ban
  result_report?: enum[ignore, Unchecked, Remove, UserBan]
  reason: string
  create_at: string
  review_id: string
  review_user_id: string
}
```

***

### [DELETE]/review_rating/reports/{id}/

- Security  
jwtAuth  

#### Responses

- 204 No response body

***

### [POST]/review_rating/reports/add_report/

- Security  
jwtAuth  

#### RequestBody

- application/json

```ts
{
  id: string
  // * `sexual` - SEXUAL
  // * `violence` - VIOLENCE
  // * `accusations` - ACCUSATIONS
  // * `terrorism` - TERRORISM
  reason_select: enum[sexual, violence, accusations, terrorism]
  // * `ignore` - Ignore
  // * `Unchecked` - Unchecked
  // * `Remove` - Remove
  // * `UserBan` - User_Ban
  result_report?: enum[ignore, Unchecked, Remove, UserBan]
  reason: string
  create_at: string
  review_id: string
  review_user_id: string
}
```

- application/x-www-form-urlencoded

```ts
{
  id: string
  // * `sexual` - SEXUAL
  // * `violence` - VIOLENCE
  // * `accusations` - ACCUSATIONS
  // * `terrorism` - TERRORISM
  reason_select: enum[sexual, violence, accusations, terrorism]
  // * `ignore` - Ignore
  // * `Unchecked` - Unchecked
  // * `Remove` - Remove
  // * `UserBan` - User_Ban
  result_report?: enum[ignore, Unchecked, Remove, UserBan]
  reason: string
  create_at: string
  review_id: string
  review_user_id: string
}
```

- multipart/form-data

```ts
{
  id: string
  // * `sexual` - SEXUAL
  // * `violence` - VIOLENCE
  // * `accusations` - ACCUSATIONS
  // * `terrorism` - TERRORISM
  reason_select: enum[sexual, violence, accusations, terrorism]
  // * `ignore` - Ignore
  // * `Unchecked` - Unchecked
  // * `Remove` - Remove
  // * `UserBan` - User_Ban
  result_report?: enum[ignore, Unchecked, Remove, UserBan]
  reason: string
  create_at: string
  review_id: string
  review_user_id: string
}
```

#### Responses

- 200 

`application/json`

```ts
{
  id: string
  // * `sexual` - SEXUAL
  // * `violence` - VIOLENCE
  // * `accusations` - ACCUSATIONS
  // * `terrorism` - TERRORISM
  reason_select: enum[sexual, violence, accusations, terrorism]
  // * `ignore` - Ignore
  // * `Unchecked` - Unchecked
  // * `Remove` - Remove
  // * `UserBan` - User_Ban
  result_report?: enum[ignore, Unchecked, Remove, UserBan]
  reason: string
  create_at: string
  review_id: string
  review_user_id: string
}
```

***

### [GET]/review_rating/review_responses/

- Security  
jwtAuth  

#### Parameters(Query)

```ts
ordering?: string
```

```ts
search?: string
```

#### Responses

- 200 

`application/json`

```ts
{
  id: string
  description: string
  created_at: string
  review: string
}[]
```

***

### [POST]/review_rating/review_responses/

- Security  
jwtAuth  

#### RequestBody

- application/json

```ts
{
  id: string
  description: string
  created_at: string
  review: string
}
```

- application/x-www-form-urlencoded

```ts
{
  id: string
  description: string
  created_at: string
  review: string
}
```

- multipart/form-data

```ts
{
  id: string
  description: string
  created_at: string
  review: string
}
```

#### Responses

- 201 

`application/json`

```ts
{
  id: string
  description: string
  created_at: string
  review: string
}
```

***

### [GET]/review_rating/review_responses/{id}/

- Security  
jwtAuth  

#### Responses

- 200 

`application/json`

```ts
{
  id: string
  description: string
  created_at: string
  review: string
}
```

***

### [PUT]/review_rating/review_responses/{id}/

- Security  
jwtAuth  

#### RequestBody

- application/json

```ts
{
  id: string
  description: string
  created_at: string
  review: string
}
```

- application/x-www-form-urlencoded

```ts
{
  id: string
  description: string
  created_at: string
  review: string
}
```

- multipart/form-data

```ts
{
  id: string
  description: string
  created_at: string
  review: string
}
```

#### Responses

- 200 

`application/json`

```ts
{
  id: string
  description: string
  created_at: string
  review: string
}
```

***

### [PATCH]/review_rating/review_responses/{id}/

- Security  
jwtAuth  

#### RequestBody

- application/json

```ts
{
  id?: string
  description?: string
  created_at?: string
  review?: string
}
```

- application/x-www-form-urlencoded

```ts
{
  id?: string
  description?: string
  created_at?: string
  review?: string
}
```

- multipart/form-data

```ts
{
  id?: string
  description?: string
  created_at?: string
  review?: string
}
```

#### Responses

- 200 

`application/json`

```ts
{
  id: string
  description: string
  created_at: string
  review: string
}
```

***

### [DELETE]/review_rating/review_responses/{id}/

- Security  
jwtAuth  

#### Responses

- 204 No response body

***

### [GET]/review_rating/reviews/

- Security  
jwtAuth  
undefined  

#### Parameters(Query)

```ts
ordering?: string
```

```ts
search?: string
```

#### Responses

- 200 

`application/json`

```ts
{
  id: string
  rank?: #/components/schemas/RankEnum
  review_text: string
  hidden?: boolean
  created_at: string
  updated_at: string
  user: string
  business_id: string
}[]
```

***

### [POST]/review_rating/reviews/

- Security  
jwtAuth  

#### RequestBody

- application/json

```ts
{
  id: string
  rank?: #/components/schemas/RankEnum
  review_text: string
  hidden?: boolean
  created_at: string
  updated_at: string
  user: string
  business_id: string
}
```

- application/x-www-form-urlencoded

```ts
{
  id: string
  rank?: #/components/schemas/RankEnum
  review_text: string
  hidden?: boolean
  created_at: string
  updated_at: string
  user: string
  business_id: string
}
```

- multipart/form-data

```ts
{
  id: string
  rank?: #/components/schemas/RankEnum
  review_text: string
  hidden?: boolean
  created_at: string
  updated_at: string
  user: string
  business_id: string
}
```

#### Responses

- 201 

`application/json`

```ts
{
  id: string
  rank?: #/components/schemas/RankEnum
  review_text: string
  hidden?: boolean
  created_at: string
  updated_at: string
  user: string
  business_id: string
}
```

***

### [GET]/review_rating/reviews/{id}/

- Security  
jwtAuth  
undefined  

#### Responses

- 200 

`application/json`

```ts
{
  id: string
  rank?: #/components/schemas/RankEnum
  review_text: string
  hidden?: boolean
  created_at: string
  updated_at: string
  user: string
  business_id: string
}
```

***

### [PUT]/review_rating/reviews/{id}/

- Security  
jwtAuth  

#### RequestBody

- application/json

```ts
{
  id: string
  rank?: #/components/schemas/RankEnum
  review_text: string
  hidden?: boolean
  created_at: string
  updated_at: string
  user: string
  business_id: string
}
```

- application/x-www-form-urlencoded

```ts
{
  id: string
  rank?: #/components/schemas/RankEnum
  review_text: string
  hidden?: boolean
  created_at: string
  updated_at: string
  user: string
  business_id: string
}
```

- multipart/form-data

```ts
{
  id: string
  rank?: #/components/schemas/RankEnum
  review_text: string
  hidden?: boolean
  created_at: string
  updated_at: string
  user: string
  business_id: string
}
```

#### Responses

- 200 

`application/json`

```ts
{
  id: string
  rank?: #/components/schemas/RankEnum
  review_text: string
  hidden?: boolean
  created_at: string
  updated_at: string
  user: string
  business_id: string
}
```

***

### [PATCH]/review_rating/reviews/{id}/

- Security  
jwtAuth  

#### RequestBody

- application/json

```ts
{
  id?: string
  rank?: #/components/schemas/RankEnum
  review_text?: string
  hidden?: boolean
  created_at?: string
  updated_at?: string
  user?: string
  business_id?: string
}
```

- application/x-www-form-urlencoded

```ts
{
  id?: string
  rank?: #/components/schemas/RankEnum
  review_text?: string
  hidden?: boolean
  created_at?: string
  updated_at?: string
  user?: string
  business_id?: string
}
```

- multipart/form-data

```ts
{
  id?: string
  rank?: #/components/schemas/RankEnum
  review_text?: string
  hidden?: boolean
  created_at?: string
  updated_at?: string
  user?: string
  business_id?: string
}
```

#### Responses

- 200 

`application/json`

```ts
{
  id: string
  rank?: #/components/schemas/RankEnum
  review_text: string
  hidden?: boolean
  created_at: string
  updated_at: string
  user: string
  business_id: string
}
```

***

### [DELETE]/review_rating/reviews/{id}/

- Security  
jwtAuth  

#### Responses

- 204 No response body

***

### [POST]/review_rating/reviews/add_review/

- Security  
jwtAuth  

#### RequestBody

- application/json

```ts
{
  id: string
  rank?: #/components/schemas/RankEnum
  review_text: string
  hidden?: boolean
  created_at: string
  updated_at: string
  user: string
  business_id: string
}
```

- application/x-www-form-urlencoded

```ts
{
  id: string
  rank?: #/components/schemas/RankEnum
  review_text: string
  hidden?: boolean
  created_at: string
  updated_at: string
  user: string
  business_id: string
}
```

- multipart/form-data

```ts
{
  id: string
  rank?: #/components/schemas/RankEnum
  review_text: string
  hidden?: boolean
  created_at: string
  updated_at: string
  user: string
  business_id: string
}
```

#### Responses

- 200 

`application/json`

```ts
{
  id: string
  rank?: #/components/schemas/RankEnum
  review_text: string
  hidden?: boolean
  created_at: string
  updated_at: string
  user: string
  business_id: string
}
```

***

### [GET]/review_rating/reviews/average-rating/

- Security  
jwtAuth  

#### Responses

- 200 

`application/json`

```ts
{
  id: string
  rank?: #/components/schemas/RankEnum
  review_text: string
  hidden?: boolean
  created_at: string
  updated_at: string
  user: string
  business_id: string
}
```

***

### [GET]/review_rating/reviews/count-all-reviews/

- Security  
jwtAuth  

#### Responses

- 200 

`application/json`

```ts
{
  id: string
  rank?: #/components/schemas/RankEnum
  review_text: string
  hidden?: boolean
  created_at: string
  updated_at: string
  user: string
  business_id: string
}
```

***

### [GET]/review_rating/reviews/count-unapproved-reviews/

- Security  
jwtAuth  

#### Responses

- 200 

`application/json`

```ts
{
  id: string
  rank?: #/components/schemas/RankEnum
  review_text: string
  hidden?: boolean
  created_at: string
  updated_at: string
  user: string
  business_id: string
}
```

***

### [GET]/review_rating/reviews/reviews-by-user/

- Security  
jwtAuth  

#### Parameters(Query)

```ts
id?: string
```

```ts
ordering?: string
```

```ts
search?: string
```

```ts
username?: string
```

#### Responses

- 200 

`application/json`

```ts
{
  id: string
  rank?: #/components/schemas/RankEnum
  review_text: string
  hidden?: boolean
  created_at: string
  updated_at: string
  user: string
  business_id: string
}[]
```

- 400 

`application/json`

```ts
// Unspecified response body
{
}
```

- 404 

`application/json`

```ts
// Unspecified response body
{
}
```

***

### [GET]/review_rating/reviews/view_reviews/

- Security  
jwtAuth  
undefined  

#### Responses

- 200 

`application/json`

```ts
{
  id: string
  rank?: #/components/schemas/RankEnum
  review_text: string
  hidden?: boolean
  created_at: string
  updated_at: string
  user: string
  business_id: string
}
```

***

### [GET]/review_rating/reviews/waiting-approval-reviews/

- Security  
jwtAuth  

#### Responses

- 200 

`application/json`

```ts
{
  id: string
  rank?: #/components/schemas/RankEnum
  review_text: string
  hidden?: boolean
  created_at: string
  updated_at: string
  user: string
  business_id: string
}
```

***

### [GET]/review_rating/votes/

- Security  
jwtAuth  

#### Parameters(Query)

```ts
ordering?: string
```

```ts
search?: string
```

#### Responses

- 200 

`application/json`

```ts
{
  id: string
  created_at: string
  user: string
  review: string
}[]
```

***

### [POST]/review_rating/votes/

- Security  
jwtAuth  

#### RequestBody

- application/json

```ts
{
  id: string
  created_at: string
  user: string
  review: string
}
```

- application/x-www-form-urlencoded

```ts
{
  id: string
  created_at: string
  user: string
  review: string
}
```

- multipart/form-data

```ts
{
  id: string
  created_at: string
  user: string
  review: string
}
```

#### Responses

- 201 

`application/json`

```ts
{
  id: string
  created_at: string
  user: string
  review: string
}
```

***

### [GET]/review_rating/votes/{id}/

- Security  
jwtAuth  

#### Responses

- 200 

`application/json`

```ts
{
  id: string
  created_at: string
  user: string
  review: string
}
```

***

### [PUT]/review_rating/votes/{id}/

- Security  
jwtAuth  

#### RequestBody

- application/json

```ts
{
  id: string
  created_at: string
  user: string
  review: string
}
```

- application/x-www-form-urlencoded

```ts
{
  id: string
  created_at: string
  user: string
  review: string
}
```

- multipart/form-data

```ts
{
  id: string
  created_at: string
  user: string
  review: string
}
```

#### Responses

- 200 

`application/json`

```ts
{
  id: string
  created_at: string
  user: string
  review: string
}
```

***

### [PATCH]/review_rating/votes/{id}/

- Security  
jwtAuth  

#### RequestBody

- application/json

```ts
{
  id?: string
  created_at?: string
  user?: string
  review?: string
}
```

- application/x-www-form-urlencoded

```ts
{
  id?: string
  created_at?: string
  user?: string
  review?: string
}
```

- multipart/form-data

```ts
{
  id?: string
  created_at?: string
  user?: string
  review?: string
}
```

#### Responses

- 200 

`application/json`

```ts
{
  id: string
  created_at: string
  user: string
  review: string
}
```

***

### [DELETE]/review_rating/votes/{id}/

- Security  
jwtAuth  

#### Responses

- 204 No response body

***

### [GET]/review_rating/votes/reviews-liked-by-user/

- Security  
jwtAuth  

#### Parameters(Query)

```ts
id?: string
```

```ts
ordering?: string
```

```ts
search?: string
```

```ts
username?: string
```

#### Responses

- 200 

`application/json`

```ts
{
  id: string
  rank?: #/components/schemas/RankEnum
  review_text: string
  hidden?: boolean
  created_at: string
  updated_at: string
  user: string
  business_id: string
}[]
```

- 400 

`application/json`

```ts
// Unspecified response body
{
}
```

- 404 

`application/json`

```ts
// Unspecified response body
{
}
```

***

### [GET]/user_management/notifications/

- Security  
jwtAuth  

#### Parameters(Query)

```ts
ordering?: string
```

```ts
search?: string
```

#### Responses

- 200 

`application/json`

```ts
{
  id: string
  is_read?: boolean
  notofication_text: string
  created_at: string
  user_notifications: string
}[]
```

***

### [POST]/user_management/notifications/

- Security  
jwtAuth  

#### RequestBody

- application/json

```ts
{
  id: string
  is_read?: boolean
  notofication_text: string
  created_at: string
  user_notifications: string
}
```

- application/x-www-form-urlencoded

```ts
{
  id: string
  is_read?: boolean
  notofication_text: string
  created_at: string
  user_notifications: string
}
```

- multipart/form-data

```ts
{
  id: string
  is_read?: boolean
  notofication_text: string
  created_at: string
  user_notifications: string
}
```

#### Responses

- 201 

`application/json`

```ts
{
  id: string
  is_read?: boolean
  notofication_text: string
  created_at: string
  user_notifications: string
}
```

***

### [GET]/user_management/notifications/{id}/

- Security  
jwtAuth  

#### Responses

- 200 

`application/json`

```ts
{
  id: string
  is_read?: boolean
  notofication_text: string
  created_at: string
  user_notifications: string
}
```

***

### [PUT]/user_management/notifications/{id}/

- Security  
jwtAuth  

#### RequestBody

- application/json

```ts
{
  id: string
  is_read?: boolean
  notofication_text: string
  created_at: string
  user_notifications: string
}
```

- application/x-www-form-urlencoded

```ts
{
  id: string
  is_read?: boolean
  notofication_text: string
  created_at: string
  user_notifications: string
}
```

- multipart/form-data

```ts
{
  id: string
  is_read?: boolean
  notofication_text: string
  created_at: string
  user_notifications: string
}
```

#### Responses

- 200 

`application/json`

```ts
{
  id: string
  is_read?: boolean
  notofication_text: string
  created_at: string
  user_notifications: string
}
```

***

### [PATCH]/user_management/notifications/{id}/

- Security  
jwtAuth  

#### RequestBody

- application/json

```ts
{
  id?: string
  is_read?: boolean
  notofication_text?: string
  created_at?: string
  user_notifications?: string
}
```

- application/x-www-form-urlencoded

```ts
{
  id?: string
  is_read?: boolean
  notofication_text?: string
  created_at?: string
  user_notifications?: string
}
```

- multipart/form-data

```ts
{
  id?: string
  is_read?: boolean
  notofication_text?: string
  created_at?: string
  user_notifications?: string
}
```

#### Responses

- 200 

`application/json`

```ts
{
  id: string
  is_read?: boolean
  notofication_text: string
  created_at: string
  user_notifications: string
}
```

***

### [DELETE]/user_management/notifications/{id}/

- Security  
jwtAuth  

#### Responses

- 204 No response body

***

### [GET]/user_management/users/

- Security  
jwtAuth  

#### Parameters(Query)

```ts
ordering?: string
```

```ts
search?: string
```

#### Responses

- 200 

`application/json`

```ts
{
  id: string
  email: string
  // Ehsan
  username: string
  user_image?: string
  // First Name
  first_name?: string
  // Last Name
  last_name?: string
  password?: string
  is_active?: boolean
  is_admin?: boolean
  hidden?: boolean
  is_superuser?: boolean
  created_at: string
}[]
```

***

### [POST]/user_management/users/

- Security  
jwtAuth  
undefined  

#### RequestBody

- application/json

```ts
{
  id: string
  email: string
  // Ehsan
  username: string
  user_image?: string
  // First Name
  first_name?: string
  // Last Name
  last_name?: string
  password?: string
  is_active?: boolean
  is_admin?: boolean
  hidden?: boolean
  is_superuser?: boolean
  created_at: string
}
```

- application/x-www-form-urlencoded

```ts
{
  id: string
  email: string
  // Ehsan
  username: string
  user_image?: string
  // First Name
  first_name?: string
  // Last Name
  last_name?: string
  password?: string
  is_active?: boolean
  is_admin?: boolean
  hidden?: boolean
  is_superuser?: boolean
  created_at: string
}
```

- multipart/form-data

```ts
{
  id: string
  email: string
  // Ehsan
  username: string
  user_image?: string
  // First Name
  first_name?: string
  // Last Name
  last_name?: string
  password?: string
  is_active?: boolean
  is_admin?: boolean
  hidden?: boolean
  is_superuser?: boolean
  created_at: string
}
```

#### Responses

- 201 

`application/json`

```ts
{
  id: string
  email: string
  // Ehsan
  username: string
  user_image?: string
  // First Name
  first_name?: string
  // Last Name
  last_name?: string
  password?: string
  is_active?: boolean
  is_admin?: boolean
  hidden?: boolean
  is_superuser?: boolean
  created_at: string
}
```

***

### [GET]/user_management/users/{id}/

- Security  
jwtAuth  

#### Responses

- 200 

`application/json`

```ts
{
  id: string
  email: string
  // Ehsan
  username: string
  user_image?: string
  // First Name
  first_name?: string
  // Last Name
  last_name?: string
  password?: string
  is_active?: boolean
  is_admin?: boolean
  hidden?: boolean
  is_superuser?: boolean
  created_at: string
}
```

***

### [PUT]/user_management/users/{id}/

- Security  
jwtAuth  

#### RequestBody

- application/json

```ts
{
  id: string
  email: string
  // Ehsan
  username: string
  user_image?: string
  // First Name
  first_name?: string
  // Last Name
  last_name?: string
  password?: string
  is_active?: boolean
  is_admin?: boolean
  hidden?: boolean
  is_superuser?: boolean
  created_at: string
}
```

- application/x-www-form-urlencoded

```ts
{
  id: string
  email: string
  // Ehsan
  username: string
  user_image?: string
  // First Name
  first_name?: string
  // Last Name
  last_name?: string
  password?: string
  is_active?: boolean
  is_admin?: boolean
  hidden?: boolean
  is_superuser?: boolean
  created_at: string
}
```

- multipart/form-data

```ts
{
  id: string
  email: string
  // Ehsan
  username: string
  user_image?: string
  // First Name
  first_name?: string
  // Last Name
  last_name?: string
  password?: string
  is_active?: boolean
  is_admin?: boolean
  hidden?: boolean
  is_superuser?: boolean
  created_at: string
}
```

#### Responses

- 200 

`application/json`

```ts
{
  id: string
  email: string
  // Ehsan
  username: string
  user_image?: string
  // First Name
  first_name?: string
  // Last Name
  last_name?: string
  password?: string
  is_active?: boolean
  is_admin?: boolean
  hidden?: boolean
  is_superuser?: boolean
  created_at: string
}
```

***

### [PATCH]/user_management/users/{id}/

- Security  
jwtAuth  

#### RequestBody

- application/json

```ts
{
  id?: string
  email?: string
  // Ehsan
  username?: string
  user_image?: string
  // First Name
  first_name?: string
  // Last Name
  last_name?: string
  password?: string
  is_active?: boolean
  is_admin?: boolean
  hidden?: boolean
  is_superuser?: boolean
  created_at?: string
}
```

- application/x-www-form-urlencoded

```ts
{
  id?: string
  email?: string
  // Ehsan
  username?: string
  user_image?: string
  // First Name
  first_name?: string
  // Last Name
  last_name?: string
  password?: string
  is_active?: boolean
  is_admin?: boolean
  hidden?: boolean
  is_superuser?: boolean
  created_at?: string
}
```

- multipart/form-data

```ts
{
  id?: string
  email?: string
  // Ehsan
  username?: string
  user_image?: string
  // First Name
  first_name?: string
  // Last Name
  last_name?: string
  password?: string
  is_active?: boolean
  is_admin?: boolean
  hidden?: boolean
  is_superuser?: boolean
  created_at?: string
}
```

#### Responses

- 200 

`application/json`

```ts
{
  id: string
  email: string
  // Ehsan
  username: string
  user_image?: string
  // First Name
  first_name?: string
  // Last Name
  last_name?: string
  password?: string
  is_active?: boolean
  is_admin?: boolean
  hidden?: boolean
  is_superuser?: boolean
  created_at: string
}
```

***

### [DELETE]/user_management/users/{id}/

- Security  
jwtAuth  

#### Responses

- 204 No response body

***

### [POST]/user_management/users/{id}/update-password/

- Security  
jwtAuth  

#### RequestBody

- application/json

```ts
{
  id: string
  email: string
  // Ehsan
  username: string
  user_image?: string
  // First Name
  first_name?: string
  // Last Name
  last_name?: string
  password?: string
  is_active?: boolean
  is_admin?: boolean
  hidden?: boolean
  is_superuser?: boolean
  created_at: string
}
```

- application/x-www-form-urlencoded

```ts
{
  id: string
  email: string
  // Ehsan
  username: string
  user_image?: string
  // First Name
  first_name?: string
  // Last Name
  last_name?: string
  password?: string
  is_active?: boolean
  is_admin?: boolean
  hidden?: boolean
  is_superuser?: boolean
  created_at: string
}
```

- multipart/form-data

```ts
{
  id: string
  email: string
  // Ehsan
  username: string
  user_image?: string
  // First Name
  first_name?: string
  // Last Name
  last_name?: string
  password?: string
  is_active?: boolean
  is_admin?: boolean
  hidden?: boolean
  is_superuser?: boolean
  created_at: string
}
```

#### Responses

- 200 

`application/json`

```ts
{
  id: string
  email: string
  // Ehsan
  username: string
  user_image?: string
  // First Name
  first_name?: string
  // Last Name
  last_name?: string
  password?: string
  is_active?: boolean
  is_admin?: boolean
  hidden?: boolean
  is_superuser?: boolean
  created_at: string
}
```

***

### [GET]/user_management/users/active-users/

- Security  
jwtAuth  

#### Responses

- 200 

`application/json`

```ts
{
  id: string
  email: string
  // Ehsan
  username: string
  user_image?: string
  // First Name
  first_name?: string
  // Last Name
  last_name?: string
  password?: string
  is_active?: boolean
  is_admin?: boolean
  hidden?: boolean
  is_superuser?: boolean
  created_at: string
}
```

***

### [GET]/user_management/users/fetch-by-username/

- Security  
jwtAuth  

#### Parameters(Query)

```ts
username: string
```

#### Responses

- 200 

`application/json`

```ts
{
  id: string
  email: string
  // Ehsan
  username: string
  user_image?: string
  // First Name
  first_name?: string
  // Last Name
  last_name?: string
  password?: string
  is_active?: boolean
  is_admin?: boolean
  hidden?: boolean
  is_superuser?: boolean
  created_at: string
}
```

- 400 

`application/json`

```ts
// Unspecified response body
{
}
```

- 404 

`application/json`

```ts
// Unspecified response body
{
}
```

***

### [GET]/user_management/users/inactive-users/

- Security  
jwtAuth  

#### Responses

- 200 

`application/json`

```ts
{
  id: string
  email: string
  // Ehsan
  username: string
  user_image?: string
  // First Name
  first_name?: string
  // Last Name
  last_name?: string
  password?: string
  is_active?: boolean
  is_admin?: boolean
  hidden?: boolean
  is_superuser?: boolean
  created_at: string
}
```

***

### [GET]/user_management/users/me/

- Security  
jwtAuth  

#### Responses

- 200 

`application/json`

```ts
{
  id: string
  email: string
  // Ehsan
  username: string
  user_image?: string
  // First Name
  first_name?: string
  // Last Name
  last_name?: string
  password?: string
  is_active?: boolean
  is_admin?: boolean
  hidden?: boolean
  is_superuser?: boolean
  created_at: string
}
```

***

### [GET]/user_management/users/total-users/

- Security  
jwtAuth  

#### Responses

- 200 

`application/json`

```ts
{
  id: string
  email: string
  // Ehsan
  username: string
  user_image?: string
  // First Name
  first_name?: string
  // Last Name
  last_name?: string
  password?: string
  is_active?: boolean
  is_admin?: boolean
  hidden?: boolean
  is_superuser?: boolean
  created_at: string
}
```

***

### [GET]/user_management/users/user-review-count/

- Security  
jwtAuth  

#### Parameters(Query)

```ts
user_id: string
```

#### Responses

- 200 

`application/json`

```ts
// Unspecified response body
{
}
```

## References

### #/components/schemas/AuditLog

```ts
{
  id: string
  content_type: string
  user: string
  action_time: string
  action_type: string
  object_id: string
  changes?: string
  ip_address?: string
  user_agent?: string
}
```

### #/components/schemas/Business

```ts
{
  id: string
  average_rating: string
  total_reviews: string
  business_image_url: string
  business_image?: string
  business_name: string
  description: string
  website_url?: string
  average_rank: integer
  created_at: string
  updated_at: string
  business_category?: string
  business_owner: string
}
```

### #/components/schemas/BusinessCreate

```ts
{
  business_image?: string
  business_owner: string
  business_name: string
  description: string
  website_url?: string
  business_category?: string
}
```

### #/components/schemas/BusinessUpdate

```ts
{
  business_image?: string
  business_owner: string
  business_name: string
  description: string
  website_url?: string
}
```

### #/components/schemas/Category

```ts
{
  id: string
  category_name: string
  category_image?: string
}
```

### #/components/schemas/FeatureRequest

```ts
{
  id: string
  description: string
  // * `pending` - PENDING
  // * `approved` - APPROVED
  // * `rejected` - REJECTED
  status?: enum[pending, approved, rejected]
  user: string
}
```

### #/components/schemas/Notification

```ts
{
  id: string
  is_read?: boolean
  notofication_text: string
  created_at: string
  user_notifications: string
}
```

### #/components/schemas/PatchedBusinessUpdate

```ts
{
  business_image?: string
  business_owner?: string
  business_name?: string
  description?: string
  website_url?: string
}
```

### #/components/schemas/PatchedCategory

```ts
{
  id?: string
  category_name?: string
  category_image?: string
}
```

### #/components/schemas/PatchedFeatureRequest

```ts
{
  id?: string
  description?: string
  // * `pending` - PENDING
  // * `approved` - APPROVED
  // * `rejected` - REJECTED
  status?: enum[pending, approved, rejected]
  user?: string
}
```

### #/components/schemas/PatchedNotification

```ts
{
  id?: string
  is_read?: boolean
  notofication_text?: string
  created_at?: string
  user_notifications?: string
}
```

### #/components/schemas/PatchedReports

```ts
{
  id?: string
  // * `sexual` - SEXUAL
  // * `violence` - VIOLENCE
  // * `accusations` - ACCUSATIONS
  // * `terrorism` - TERRORISM
  reason_select?: enum[sexual, violence, accusations, terrorism]
  // * `ignore` - Ignore
  // * `Unchecked` - Unchecked
  // * `Remove` - Remove
  // * `UserBan` - User_Ban
  result_report?: enum[ignore, Unchecked, Remove, UserBan]
  reason?: string
  create_at?: string
  review_id?: string
  review_user_id?: string
}
```

### #/components/schemas/PatchedReview

```ts
{
  id?: string
  rank?: #/components/schemas/RankEnum
  review_text?: string
  hidden?: boolean
  created_at?: string
  updated_at?: string
  user?: string
  business_id?: string
}
```

### #/components/schemas/PatchedReviewResponse

```ts
{
  id?: string
  description?: string
  created_at?: string
  review?: string
}
```

### #/components/schemas/PatchedSubscription

```ts
{
  id?: string
  // * `free` - FREE
  // * `premium` - PREMIUM
  type?: enum[free, premium]
  start_date?: string
  end_date?: string
  is_active?: boolean
  business?: string
}
```

### #/components/schemas/PatchedUser

```ts
{
  id?: string
  email?: string
  // Ehsan
  username?: string
  user_image?: string
  // First Name
  first_name?: string
  // Last Name
  last_name?: string
  password?: string
  is_active?: boolean
  is_admin?: boolean
  hidden?: boolean
  is_superuser?: boolean
  created_at?: string
}
```

### #/components/schemas/PatchedVote

```ts
{
  id?: string
  created_at?: string
  user?: string
  review?: string
}
```

### #/components/schemas/RankEnum

```ts
{
  "enum": [
    1,
    2,
    3,
    4,
    5
  ],
  "type": "integer",
  "description": "* `1` - Very Poor\n* `2` - Poor\n* `3` - Medium\n* `4` - Good\n* `5` - Very Good"
}
```

### #/components/schemas/ReasonSelectEnum

```ts
{
  "enum": [
    "sexual",
    "violence",
    "accusations",
    "terrorism"
  ],
  "type": "string",
  "description": "* `sexual` - SEXUAL\n* `violence` - VIOLENCE\n* `accusations` - ACCUSATIONS\n* `terrorism` - TERRORISM"
}
```

### #/components/schemas/Reports

```ts
{
  id: string
  // * `sexual` - SEXUAL
  // * `violence` - VIOLENCE
  // * `accusations` - ACCUSATIONS
  // * `terrorism` - TERRORISM
  reason_select: enum[sexual, violence, accusations, terrorism]
  // * `ignore` - Ignore
  // * `Unchecked` - Unchecked
  // * `Remove` - Remove
  // * `UserBan` - User_Ban
  result_report?: enum[ignore, Unchecked, Remove, UserBan]
  reason: string
  create_at: string
  review_id: string
  review_user_id: string
}
```

### #/components/schemas/ResultReportEnum

```ts
{
  "enum": [
    "ignore",
    "Unchecked",
    "Remove",
    "UserBan"
  ],
  "type": "string",
  "description": "* `ignore` - Ignore\n* `Unchecked` - Unchecked\n* `Remove` - Remove\n* `UserBan` - User_Ban"
}
```

### #/components/schemas/Review

```ts
{
  id: string
  rank?: #/components/schemas/RankEnum
  review_text: string
  hidden?: boolean
  created_at: string
  updated_at: string
  user: string
  business_id: string
}
```

### #/components/schemas/ReviewResponse

```ts
{
  id: string
  description: string
  created_at: string
  review: string
}
```

### #/components/schemas/StatusEnum

```ts
{
  "enum": [
    "pending",
    "approved",
    "rejected"
  ],
  "type": "string",
  "description": "* `pending` - PENDING\n* `approved` - APPROVED\n* `rejected` - REJECTED"
}
```

### #/components/schemas/Subscription

```ts
{
  id: string
  // * `free` - FREE
  // * `premium` - PREMIUM
  type?: enum[free, premium]
  start_date: string
  end_date: string
  is_active?: boolean
  business: string
}
```

### #/components/schemas/TokenObtainPair

```ts
{
  username: string
  password: string
  access: string
  refresh: string
}
```

### #/components/schemas/TokenRefresh

```ts
{
  access: string
  refresh: string
}
```

### #/components/schemas/TypeEnum

```ts
{
  "enum": [
    "free",
    "premium"
  ],
  "type": "string",
  "description": "* `free` - FREE\n* `premium` - PREMIUM"
}
```

### #/components/schemas/User

```ts
{
  id: string
  email: string
  // Ehsan
  username: string
  user_image?: string
  // First Name
  first_name?: string
  // Last Name
  last_name?: string
  password?: string
  is_active?: boolean
  is_admin?: boolean
  hidden?: boolean
  is_superuser?: boolean
  created_at: string
}
```

### #/components/schemas/Vote

```ts
{
  id: string
  created_at: string
  user: string
  review: string
}
```

### #/components/securitySchemes/jwtAuth

```ts
{
  "type": "http",
  "scheme": "bearer",
  "bearerFormat": "JWT"
}
```



