-- This script was generated by the ERD tool in pgAdmin 4.
-- Please log an issue at https://redmine.postgresql.org/projects/pgadmin4/issues/new if you find any bugs, including reproduction steps.
BEGIN;


CREATE TABLE IF NOT EXISTS public.analytics_auditlog
(
    id uuid NOT NULL,
    action_time timestamp with time zone NOT NULL,
    action_type character varying(50) COLLATE pg_catalog."default" NOT NULL,
    object_id character varying(50) COLLATE pg_catalog."default" NOT NULL,
    changes text COLLATE pg_catalog."default",
    ip_address inet,
    user_agent text COLLATE pg_catalog."default",
    content_type_id integer NOT NULL,
    user_id uuid,
    CONSTRAINT analytics_auditlog_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.auth_group
(
    id integer NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    name character varying(150) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT auth_group_pkey PRIMARY KEY (id),
    CONSTRAINT auth_group_name_key UNIQUE (name)
);

CREATE TABLE IF NOT EXISTS public.auth_group_permissions
(
    id bigint NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    group_id integer NOT NULL,
    permission_id integer NOT NULL,
    CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id),
    CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id)
);

CREATE TABLE IF NOT EXISTS public.auth_permission
(
    id integer NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    name character varying(255) COLLATE pg_catalog."default" NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT auth_permission_pkey PRIMARY KEY (id),
    CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename)
);

CREATE TABLE IF NOT EXISTS public.business_management_business
(
    id uuid NOT NULL,
    business_name character varying(100) COLLATE pg_catalog."default" NOT NULL,
    description text COLLATE pg_catalog."default" NOT NULL,
    website_url character varying(50) COLLATE pg_catalog."default",
    average_rank integer NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    business_owner_id uuid NOT NULL,
    CONSTRAINT business_management_business_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.business_management_subscription
(
    id uuid NOT NULL,
    type character varying(20) COLLATE pg_catalog."default" NOT NULL,
    start_date timestamp with time zone NOT NULL,
    end_date timestamp with time zone NOT NULL,
    is_active boolean NOT NULL,
    business_id uuid NOT NULL,
    CONSTRAINT business_management_subscription_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.django_admin_log
(
    id integer NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    action_time timestamp with time zone NOT NULL,
    object_id text COLLATE pg_catalog."default",
    object_repr character varying(200) COLLATE pg_catalog."default" NOT NULL,
    action_flag smallint NOT NULL,
    change_message text COLLATE pg_catalog."default" NOT NULL,
    content_type_id integer,
    user_id uuid NOT NULL,
    CONSTRAINT django_admin_log_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.django_content_type
(
    id integer NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    app_label character varying(100) COLLATE pg_catalog."default" NOT NULL,
    model character varying(100) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT django_content_type_pkey PRIMARY KEY (id),
    CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model)
);

CREATE TABLE IF NOT EXISTS public.django_migrations
(
    id bigint NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    app character varying(255) COLLATE pg_catalog."default" NOT NULL,
    name character varying(255) COLLATE pg_catalog."default" NOT NULL,
    applied timestamp with time zone NOT NULL,
    CONSTRAINT django_migrations_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.django_session
(
    session_key character varying(40) COLLATE pg_catalog."default" NOT NULL,
    session_data text COLLATE pg_catalog."default" NOT NULL,
    expire_date timestamp with time zone NOT NULL,
    CONSTRAINT django_session_pkey PRIMARY KEY (session_key)
);

CREATE TABLE IF NOT EXISTS public.platform_management_featurerequest
(
    id uuid NOT NULL,
    description text COLLATE pg_catalog."default" NOT NULL,
    status character varying(20) COLLATE pg_catalog."default" NOT NULL,
    user_id uuid NOT NULL,
    CONSTRAINT platform_management_featurerequest_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.review_rating_reports
(
    id uuid NOT NULL,
    reason_select character varying(20) COLLATE pg_catalog."default" NOT NULL,
    reason text COLLATE pg_catalog."default" NOT NULL,
    create_at timestamp with time zone NOT NULL,
    review_id_id uuid NOT NULL,
    review_user_id_id uuid NOT NULL,
    CONSTRAINT review_rating_reports_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.review_rating_review
(
    id uuid NOT NULL,
    rank integer NOT NULL,
    review_text text COLLATE pg_catalog."default" NOT NULL,
    hidden boolean NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    business_id_id uuid NOT NULL,
    user_id uuid NOT NULL,
    CONSTRAINT review_rating_review_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.review_rating_reviewresponse
(
    id uuid NOT NULL,
    description text COLLATE pg_catalog."default" NOT NULL,
    created_at timestamp with time zone NOT NULL,
    review_id uuid NOT NULL,
    CONSTRAINT review_rating_reviewresponse_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.review_rating_vote
(
    id uuid NOT NULL,
    created_at timestamp with time zone NOT NULL,
    review_id uuid NOT NULL,
    user_id uuid NOT NULL,
    CONSTRAINT review_rating_vote_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.user_management_notifications
(
    id uuid NOT NULL,
    is_read boolean NOT NULL,
    notofication_text text COLLATE pg_catalog."default" NOT NULL,
    created_at timestamp with time zone NOT NULL,
    user_notifications_id uuid NOT NULL,
    CONSTRAINT user_management_notifications_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.user_management_user
(
    password character varying(128) COLLATE pg_catalog."default" NOT NULL,
    last_login timestamp with time zone,
    id uuid NOT NULL,
    email character varying(30) COLLATE pg_catalog."default" NOT NULL,
    username character varying(50) COLLATE pg_catalog."default" NOT NULL,
    hidden boolean NOT NULL,
    is_active boolean NOT NULL,
    is_admin boolean NOT NULL,
    created_at timestamp with time zone NOT NULL,
    is_superuser boolean NOT NULL,
    CONSTRAINT user_management_user_pkey PRIMARY KEY (id),
    CONSTRAINT user_management_user_email_key UNIQUE (email),
    CONSTRAINT user_management_user_username_key UNIQUE (username)
);

CREATE TABLE IF NOT EXISTS public.user_management_user_groups
(
    id bigint NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    user_id uuid NOT NULL,
    group_id integer NOT NULL,
    CONSTRAINT user_management_user_groups_pkey PRIMARY KEY (id),
    CONSTRAINT user_management_user_groups_user_id_group_id_bed1779a_uniq UNIQUE (user_id, group_id)
);

CREATE TABLE IF NOT EXISTS public.user_management_user_user_permissions
(
    id bigint NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    user_id uuid NOT NULL,
    permission_id integer NOT NULL,
    CONSTRAINT user_management_user_user_permissions_pkey PRIMARY KEY (id),
    CONSTRAINT user_management_user_use_user_id_permission_id_c71a3268_uniq UNIQUE (user_id, permission_id)
);

ALTER TABLE IF EXISTS public.analytics_auditlog
    ADD CONSTRAINT analytics_auditlog_content_type_id_ff5548d8_fk_django_co FOREIGN KEY (content_type_id)
    REFERENCES public.django_content_type (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS analytics_auditlog_content_type_id_ff5548d8
    ON public.analytics_auditlog(content_type_id);


ALTER TABLE IF EXISTS public.analytics_auditlog
    ADD CONSTRAINT analytics_auditlog_user_id_b618215f_fk_user_management_user_id FOREIGN KEY (user_id)
    REFERENCES public.user_management_user (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS analytics_auditlog_user_id_b618215f
    ON public.analytics_auditlog(user_id);


ALTER TABLE IF EXISTS public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id)
    REFERENCES public.auth_permission (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS auth_group_permissions_permission_id_84c5c92e
    ON public.auth_group_permissions(permission_id);


ALTER TABLE IF EXISTS public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id)
    REFERENCES public.auth_group (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS auth_group_permissions_group_id_b120cbf9
    ON public.auth_group_permissions(group_id);


ALTER TABLE IF EXISTS public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id)
    REFERENCES public.django_content_type (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS auth_permission_content_type_id_2f476e4b
    ON public.auth_permission(content_type_id);


ALTER TABLE IF EXISTS public.business_management_business
    ADD CONSTRAINT business_management__business_owner_id_0cca86d9_fk_user_mana FOREIGN KEY (business_owner_id)
    REFERENCES public.user_management_user (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS business_management_business_business_owner_id_0cca86d9
    ON public.business_management_business(business_owner_id);


ALTER TABLE IF EXISTS public.business_management_subscription
    ADD CONSTRAINT business_management__business_id_60b7c7ee_fk_business_ FOREIGN KEY (business_id)
    REFERENCES public.business_management_business (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS business_management_subscription_business_id_60b7c7ee
    ON public.business_management_subscription(business_id);


ALTER TABLE IF EXISTS public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id)
    REFERENCES public.django_content_type (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS django_admin_log_content_type_id_c4bce8eb
    ON public.django_admin_log(content_type_id);


ALTER TABLE IF EXISTS public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_user_management_user_id FOREIGN KEY (user_id)
    REFERENCES public.user_management_user (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS django_admin_log_user_id_c564eba6
    ON public.django_admin_log(user_id);


ALTER TABLE IF EXISTS public.platform_management_featurerequest
    ADD CONSTRAINT platform_management__user_id_9093834f_fk_user_mana FOREIGN KEY (user_id)
    REFERENCES public.user_management_user (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS platform_management_featurerequest_user_id_9093834f
    ON public.platform_management_featurerequest(user_id);


ALTER TABLE IF EXISTS public.review_rating_reports
    ADD CONSTRAINT review_rating_report_review_id_id_b5e26a4f_fk_review_ra FOREIGN KEY (review_id_id)
    REFERENCES public.review_rating_review (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS review_rating_reports_review_id_id_b5e26a4f
    ON public.review_rating_reports(review_id_id);


ALTER TABLE IF EXISTS public.review_rating_reports
    ADD CONSTRAINT review_rating_report_review_user_id_id_af465909_fk_user_mana FOREIGN KEY (review_user_id_id)
    REFERENCES public.user_management_user (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS review_rating_reports_review_user_id_id_af465909
    ON public.review_rating_reports(review_user_id_id);


ALTER TABLE IF EXISTS public.review_rating_review
    ADD CONSTRAINT review_rating_review_business_id_id_83af63c8_fk_business_ FOREIGN KEY (business_id_id)
    REFERENCES public.business_management_business (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS review_rating_review_business_id_id_83af63c8
    ON public.review_rating_review(business_id_id);


ALTER TABLE IF EXISTS public.review_rating_review
    ADD CONSTRAINT review_rating_review_user_id_1dea6b24_fk_user_mana FOREIGN KEY (user_id)
    REFERENCES public.user_management_user (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS review_rating_review_user_id_1dea6b24
    ON public.review_rating_review(user_id);


ALTER TABLE IF EXISTS public.review_rating_reviewresponse
    ADD CONSTRAINT review_rating_review_review_id_2d39e854_fk_review_ra FOREIGN KEY (review_id)
    REFERENCES public.review_rating_review (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS review_rating_reviewresponse_review_id_2d39e854
    ON public.review_rating_reviewresponse(review_id);


ALTER TABLE IF EXISTS public.review_rating_vote
    ADD CONSTRAINT review_rating_vote_review_id_83730638_fk_review_ra FOREIGN KEY (review_id)
    REFERENCES public.review_rating_review (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS review_rating_vote_review_id_83730638
    ON public.review_rating_vote(review_id);


ALTER TABLE IF EXISTS public.review_rating_vote
    ADD CONSTRAINT review_rating_vote_user_id_7dbfa32e_fk_user_management_user_id FOREIGN KEY (user_id)
    REFERENCES public.user_management_user (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS review_rating_vote_user_id_7dbfa32e
    ON public.review_rating_vote(user_id);


ALTER TABLE IF EXISTS public.user_management_notifications
    ADD CONSTRAINT user_management_noti_user_notifications_i_102cf2e4_fk_user_mana FOREIGN KEY (user_notifications_id)
    REFERENCES public.user_management_user (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS user_management_notifications_user_notifications_id_102cf2e4
    ON public.user_management_notifications(user_notifications_id);


ALTER TABLE IF EXISTS public.user_management_user_groups
    ADD CONSTRAINT user_management_user_groups_group_id_6f577055_fk_auth_group_id FOREIGN KEY (group_id)
    REFERENCES public.auth_group (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS user_management_user_groups_group_id_6f577055
    ON public.user_management_user_groups(group_id);


ALTER TABLE IF EXISTS public.user_management_user_groups
    ADD CONSTRAINT user_management_user_user_id_092e6f6b_fk_user_mana FOREIGN KEY (user_id)
    REFERENCES public.user_management_user (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS user_management_user_groups_user_id_092e6f6b
    ON public.user_management_user_groups(user_id);


ALTER TABLE IF EXISTS public.user_management_user_user_permissions
    ADD CONSTRAINT user_management_user_permission_id_d8c2b1e9_fk_auth_perm FOREIGN KEY (permission_id)
    REFERENCES public.auth_permission (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS user_management_user_user_permissions_permission_id_d8c2b1e9
    ON public.user_management_user_user_permissions(permission_id);


ALTER TABLE IF EXISTS public.user_management_user_user_permissions
    ADD CONSTRAINT user_management_user_user_id_4b8c2c7b_fk_user_mana FOREIGN KEY (user_id)
    REFERENCES public.user_management_user (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS user_management_user_user_permissions_user_id_4b8c2c7b
    ON public.user_management_user_user_permissions(user_id);

END;