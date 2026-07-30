import RHBridge.P2RoundedFlatFactorCheckpoint12
import RHBridge.P2RoundedMomentLengths12
import RHBridge.P2RoundedMomentCheckpointCheck12_moments
import RHBridge.P2RoundedMomentCheckpointCheck12_mode0
import RHBridge.P2RoundedMomentCheckpointCheck12_mode1
import RHBridge.P2RoundedMomentCheckpointCheck12_mode2
import RHBridge.P2RoundedMomentCheckpointCheck12_mode3
import RHBridge.P2RoundedMomentCheckpointCheck12_mode4
import RHBridge.P2RoundedMomentCheckpointCheck12_mode5
import RHBridge.P2RoundedMomentCheckpointCheck12_mode6
import RHBridge.P2RoundedMomentCheckpointCheck12_mode7
import RHBridge.P2RoundedMomentCheckpointCheck12_mode8
import RHBridge.P2RoundedMomentCheckpointCheck12_mode9
import RHBridge.P2RoundedMomentCheckpointCheck12_mode10
import RHBridge.P2RoundedMomentCheckpointCheck12_mode11
import RHBridge.P2RoundedMomentCheckpointCheck12_mode12
import RHBridge.P2RoundedMomentCheckpointCheck12_mode13
import RHBridge.P2RoundedMomentCheckpointCheck12_mode14
import RHBridge.P2RoundedMomentCheckpointCheck12_mode15
import RHBridge.P2RoundedMomentCheckpointCheck12_mode16
import RHBridge.P2RoundedMomentCheckpointCheck12_mode17
import RHBridge.P2RoundedMomentCheckpointCheck12_mode18
import RHBridge.P2RoundedMomentCheckpointCheck12_mode19
import RHBridge.P2RoundedMomentCheckpointCheck12_mode20
import RHBridge.P2RoundedMomentCheckpointCheck12_mode21
import RHBridge.P2RoundedMomentCheckpointCheck12_mode22
import RHBridge.P2RoundedMomentCheckpointCheck12_mode23
import RHBridge.P2RoundedMomentCheckpointCheck12_mode24
import RHBridge.P2RoundedMomentCheckpointCheck12_mode25
import RHBridge.P2RoundedMomentCheckpointCheck12_mode26
import RHBridge.P2RoundedMomentCheckpointCheck12_mode27
import RHBridge.P2RoundedMomentCheckpointCheck12_mode28
import RHBridge.P2RoundedMomentCheckpointCheck12_mode29
import RHBridge.P2RoundedMomentCheckpointCheck12_mode30
import RHBridge.P2RoundedMomentCheckpointCheck12_mode31
import RHBridge.P2RoundedMomentCheckpointCheck12_mode32
import RHBridge.P2RoundedMomentCheckpointCheck12_mode33
import RHBridge.P2RoundedMomentCheckpointCheck12_mode34
import RHBridge.P2RoundedMomentCheckpointCheck12_mode35
import RHBridge.P2RoundedMomentCheckpointCheck12_mode36
import RHBridge.P2RoundedMomentCheckpointCheck12_mode37
import RHBridge.P2RoundedMomentCheckpointCheck12_mode38
import RHBridge.P2RoundedMomentCheckpointCheck12_mode39
import RHBridge.P2RoundedMomentCheckpointCheck12_mode40
import RHBridge.P2RoundedMomentCheckpointCheck12_mode41
import RHBridge.P2RoundedMomentCheckpointCheck12_mode42
import RHBridge.P2RoundedMomentCheckpointCheck12_mode43
import RHBridge.P2RoundedMomentCheckpointCheck12_mode44
import RHBridge.P2RoundedMomentCheckpointCheck12_mode45
import RHBridge.P2RoundedMomentCheckpointCheck12_mode46
import RHBridge.P2RoundedMomentCheckpointCheck12_mode47

namespace RHP2Bridge

open P2RoundedSharedEvaluator
open P2RoundedMomentRefinement

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

private theorem vector_ext_fin
    {α : Type} {n : Nat} {v w : Vector α n}
    (h : ∀ i : Fin n, v.get i = w.get i) : v = w := by
  apply Vector.ext
  intro i hi
  exact h ⟨i, hi⟩

theorem panel12DefectMoments_eq :
    P2RoundedFactorCheckpointData.panel12MomentData.moments =
      P2RoundedTripleMoment.defectMoments
        P2RoundedFactorCheckpointData.panel12FlatCache.defect.coeffs := by
  apply vector_ext_fin
  intro row
  rw [P2RoundedTripleMoment.defectMoments_get]
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel12DefectMomentRange0) panel12DefectMomentRange64) panel12DefectMomentRange128) panel12DefectMomentRange192) panel12DefectMomentRange256) row

theorem panel12Mode0MatVec_eq :
    P2RoundedFactorCheckpointData.panel12MomentData.matvecs
        .even ⟨0, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel12MomentData.moments
        (P2RoundedFactorCheckpointData.panel12FlatCache.component
          .even ⟨0, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel12Mode0MatVecRange0) panel12Mode0MatVecRange32) panel12Mode0MatVecRange64) panel12Mode0MatVecRange96) panel12Mode0MatVecRange128) row

theorem panel12Mode1MatVec_eq :
    P2RoundedFactorCheckpointData.panel12MomentData.matvecs
        .odd ⟨0, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel12MomentData.moments
        (P2RoundedFactorCheckpointData.panel12FlatCache.component
          .odd ⟨0, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel12Mode1MatVecRange0) panel12Mode1MatVecRange32) panel12Mode1MatVecRange64) panel12Mode1MatVecRange96) panel12Mode1MatVecRange128) row

theorem panel12Mode2MatVec_eq :
    P2RoundedFactorCheckpointData.panel12MomentData.matvecs
        .even ⟨1, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel12MomentData.moments
        (P2RoundedFactorCheckpointData.panel12FlatCache.component
          .even ⟨1, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel12Mode2MatVecRange0) panel12Mode2MatVecRange32) panel12Mode2MatVecRange64) panel12Mode2MatVecRange96) panel12Mode2MatVecRange128) row

theorem panel12Mode3MatVec_eq :
    P2RoundedFactorCheckpointData.panel12MomentData.matvecs
        .odd ⟨1, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel12MomentData.moments
        (P2RoundedFactorCheckpointData.panel12FlatCache.component
          .odd ⟨1, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel12Mode3MatVecRange0) panel12Mode3MatVecRange32) panel12Mode3MatVecRange64) panel12Mode3MatVecRange96) panel12Mode3MatVecRange128) row

theorem panel12Mode4MatVec_eq :
    P2RoundedFactorCheckpointData.panel12MomentData.matvecs
        .even ⟨2, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel12MomentData.moments
        (P2RoundedFactorCheckpointData.panel12FlatCache.component
          .even ⟨2, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel12Mode4MatVecRange0) panel12Mode4MatVecRange32) panel12Mode4MatVecRange64) panel12Mode4MatVecRange96) panel12Mode4MatVecRange128) row

theorem panel12Mode5MatVec_eq :
    P2RoundedFactorCheckpointData.panel12MomentData.matvecs
        .odd ⟨2, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel12MomentData.moments
        (P2RoundedFactorCheckpointData.panel12FlatCache.component
          .odd ⟨2, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel12Mode5MatVecRange0) panel12Mode5MatVecRange32) panel12Mode5MatVecRange64) panel12Mode5MatVecRange96) panel12Mode5MatVecRange128) row

theorem panel12Mode6MatVec_eq :
    P2RoundedFactorCheckpointData.panel12MomentData.matvecs
        .even ⟨3, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel12MomentData.moments
        (P2RoundedFactorCheckpointData.panel12FlatCache.component
          .even ⟨3, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel12Mode6MatVecRange0) panel12Mode6MatVecRange32) panel12Mode6MatVecRange64) panel12Mode6MatVecRange96) panel12Mode6MatVecRange128) row

theorem panel12Mode7MatVec_eq :
    P2RoundedFactorCheckpointData.panel12MomentData.matvecs
        .odd ⟨3, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel12MomentData.moments
        (P2RoundedFactorCheckpointData.panel12FlatCache.component
          .odd ⟨3, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel12Mode7MatVecRange0) panel12Mode7MatVecRange32) panel12Mode7MatVecRange64) panel12Mode7MatVecRange96) panel12Mode7MatVecRange128) row

theorem panel12Mode8MatVec_eq :
    P2RoundedFactorCheckpointData.panel12MomentData.matvecs
        .even ⟨4, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel12MomentData.moments
        (P2RoundedFactorCheckpointData.panel12FlatCache.component
          .even ⟨4, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel12Mode8MatVecRange0) panel12Mode8MatVecRange32) panel12Mode8MatVecRange64) panel12Mode8MatVecRange96) panel12Mode8MatVecRange128) row

theorem panel12Mode9MatVec_eq :
    P2RoundedFactorCheckpointData.panel12MomentData.matvecs
        .odd ⟨4, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel12MomentData.moments
        (P2RoundedFactorCheckpointData.panel12FlatCache.component
          .odd ⟨4, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel12Mode9MatVecRange0) panel12Mode9MatVecRange32) panel12Mode9MatVecRange64) panel12Mode9MatVecRange96) panel12Mode9MatVecRange128) row

theorem panel12Mode10MatVec_eq :
    P2RoundedFactorCheckpointData.panel12MomentData.matvecs
        .even ⟨5, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel12MomentData.moments
        (P2RoundedFactorCheckpointData.panel12FlatCache.component
          .even ⟨5, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel12Mode10MatVecRange0) panel12Mode10MatVecRange32) panel12Mode10MatVecRange64) panel12Mode10MatVecRange96) panel12Mode10MatVecRange128) row

theorem panel12Mode11MatVec_eq :
    P2RoundedFactorCheckpointData.panel12MomentData.matvecs
        .odd ⟨5, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel12MomentData.moments
        (P2RoundedFactorCheckpointData.panel12FlatCache.component
          .odd ⟨5, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel12Mode11MatVecRange0) panel12Mode11MatVecRange32) panel12Mode11MatVecRange64) panel12Mode11MatVecRange96) panel12Mode11MatVecRange128) row

theorem panel12Mode12MatVec_eq :
    P2RoundedFactorCheckpointData.panel12MomentData.matvecs
        .even ⟨6, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel12MomentData.moments
        (P2RoundedFactorCheckpointData.panel12FlatCache.component
          .even ⟨6, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel12Mode12MatVecRange0) panel12Mode12MatVecRange32) panel12Mode12MatVecRange64) panel12Mode12MatVecRange96) panel12Mode12MatVecRange128) row

theorem panel12Mode13MatVec_eq :
    P2RoundedFactorCheckpointData.panel12MomentData.matvecs
        .odd ⟨6, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel12MomentData.moments
        (P2RoundedFactorCheckpointData.panel12FlatCache.component
          .odd ⟨6, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel12Mode13MatVecRange0) panel12Mode13MatVecRange32) panel12Mode13MatVecRange64) panel12Mode13MatVecRange96) panel12Mode13MatVecRange128) row

theorem panel12Mode14MatVec_eq :
    P2RoundedFactorCheckpointData.panel12MomentData.matvecs
        .even ⟨7, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel12MomentData.moments
        (P2RoundedFactorCheckpointData.panel12FlatCache.component
          .even ⟨7, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel12Mode14MatVecRange0) panel12Mode14MatVecRange32) panel12Mode14MatVecRange64) panel12Mode14MatVecRange96) panel12Mode14MatVecRange128) row

theorem panel12Mode15MatVec_eq :
    P2RoundedFactorCheckpointData.panel12MomentData.matvecs
        .odd ⟨7, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel12MomentData.moments
        (P2RoundedFactorCheckpointData.panel12FlatCache.component
          .odd ⟨7, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel12Mode15MatVecRange0) panel12Mode15MatVecRange32) panel12Mode15MatVecRange64) panel12Mode15MatVecRange96) panel12Mode15MatVecRange128) row

theorem panel12Mode16MatVec_eq :
    P2RoundedFactorCheckpointData.panel12MomentData.matvecs
        .even ⟨8, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel12MomentData.moments
        (P2RoundedFactorCheckpointData.panel12FlatCache.component
          .even ⟨8, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel12Mode16MatVecRange0) panel12Mode16MatVecRange32) panel12Mode16MatVecRange64) panel12Mode16MatVecRange96) panel12Mode16MatVecRange128) row

theorem panel12Mode17MatVec_eq :
    P2RoundedFactorCheckpointData.panel12MomentData.matvecs
        .odd ⟨8, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel12MomentData.moments
        (P2RoundedFactorCheckpointData.panel12FlatCache.component
          .odd ⟨8, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel12Mode17MatVecRange0) panel12Mode17MatVecRange32) panel12Mode17MatVecRange64) panel12Mode17MatVecRange96) panel12Mode17MatVecRange128) row

theorem panel12Mode18MatVec_eq :
    P2RoundedFactorCheckpointData.panel12MomentData.matvecs
        .even ⟨9, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel12MomentData.moments
        (P2RoundedFactorCheckpointData.panel12FlatCache.component
          .even ⟨9, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel12Mode18MatVecRange0) panel12Mode18MatVecRange32) panel12Mode18MatVecRange64) panel12Mode18MatVecRange96) panel12Mode18MatVecRange128) row

theorem panel12Mode19MatVec_eq :
    P2RoundedFactorCheckpointData.panel12MomentData.matvecs
        .odd ⟨9, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel12MomentData.moments
        (P2RoundedFactorCheckpointData.panel12FlatCache.component
          .odd ⟨9, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel12Mode19MatVecRange0) panel12Mode19MatVecRange32) panel12Mode19MatVecRange64) panel12Mode19MatVecRange96) panel12Mode19MatVecRange128) row

theorem panel12Mode20MatVec_eq :
    P2RoundedFactorCheckpointData.panel12MomentData.matvecs
        .even ⟨10, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel12MomentData.moments
        (P2RoundedFactorCheckpointData.panel12FlatCache.component
          .even ⟨10, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel12Mode20MatVecRange0) panel12Mode20MatVecRange32) panel12Mode20MatVecRange64) panel12Mode20MatVecRange96) panel12Mode20MatVecRange128) row

theorem panel12Mode21MatVec_eq :
    P2RoundedFactorCheckpointData.panel12MomentData.matvecs
        .odd ⟨10, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel12MomentData.moments
        (P2RoundedFactorCheckpointData.panel12FlatCache.component
          .odd ⟨10, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel12Mode21MatVecRange0) panel12Mode21MatVecRange32) panel12Mode21MatVecRange64) panel12Mode21MatVecRange96) panel12Mode21MatVecRange128) row

theorem panel12Mode22MatVec_eq :
    P2RoundedFactorCheckpointData.panel12MomentData.matvecs
        .even ⟨11, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel12MomentData.moments
        (P2RoundedFactorCheckpointData.panel12FlatCache.component
          .even ⟨11, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel12Mode22MatVecRange0) panel12Mode22MatVecRange32) panel12Mode22MatVecRange64) panel12Mode22MatVecRange96) panel12Mode22MatVecRange128) row

theorem panel12Mode23MatVec_eq :
    P2RoundedFactorCheckpointData.panel12MomentData.matvecs
        .odd ⟨11, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel12MomentData.moments
        (P2RoundedFactorCheckpointData.panel12FlatCache.component
          .odd ⟨11, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel12Mode23MatVecRange0) panel12Mode23MatVecRange32) panel12Mode23MatVecRange64) panel12Mode23MatVecRange96) panel12Mode23MatVecRange128) row

theorem panel12Mode24MatVec_eq :
    P2RoundedFactorCheckpointData.panel12MomentData.matvecs
        .even ⟨12, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel12MomentData.moments
        (P2RoundedFactorCheckpointData.panel12FlatCache.component
          .even ⟨12, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel12Mode24MatVecRange0) panel12Mode24MatVecRange32) panel12Mode24MatVecRange64) panel12Mode24MatVecRange96) panel12Mode24MatVecRange128) row

theorem panel12Mode25MatVec_eq :
    P2RoundedFactorCheckpointData.panel12MomentData.matvecs
        .odd ⟨12, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel12MomentData.moments
        (P2RoundedFactorCheckpointData.panel12FlatCache.component
          .odd ⟨12, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel12Mode25MatVecRange0) panel12Mode25MatVecRange32) panel12Mode25MatVecRange64) panel12Mode25MatVecRange96) panel12Mode25MatVecRange128) row

theorem panel12Mode26MatVec_eq :
    P2RoundedFactorCheckpointData.panel12MomentData.matvecs
        .even ⟨13, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel12MomentData.moments
        (P2RoundedFactorCheckpointData.panel12FlatCache.component
          .even ⟨13, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel12Mode26MatVecRange0) panel12Mode26MatVecRange32) panel12Mode26MatVecRange64) panel12Mode26MatVecRange96) panel12Mode26MatVecRange128) row

theorem panel12Mode27MatVec_eq :
    P2RoundedFactorCheckpointData.panel12MomentData.matvecs
        .odd ⟨13, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel12MomentData.moments
        (P2RoundedFactorCheckpointData.panel12FlatCache.component
          .odd ⟨13, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel12Mode27MatVecRange0) panel12Mode27MatVecRange32) panel12Mode27MatVecRange64) panel12Mode27MatVecRange96) panel12Mode27MatVecRange128) row

theorem panel12Mode28MatVec_eq :
    P2RoundedFactorCheckpointData.panel12MomentData.matvecs
        .even ⟨14, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel12MomentData.moments
        (P2RoundedFactorCheckpointData.panel12FlatCache.component
          .even ⟨14, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel12Mode28MatVecRange0) panel12Mode28MatVecRange32) panel12Mode28MatVecRange64) panel12Mode28MatVecRange96) panel12Mode28MatVecRange128) row

theorem panel12Mode29MatVec_eq :
    P2RoundedFactorCheckpointData.panel12MomentData.matvecs
        .odd ⟨14, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel12MomentData.moments
        (P2RoundedFactorCheckpointData.panel12FlatCache.component
          .odd ⟨14, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel12Mode29MatVecRange0) panel12Mode29MatVecRange32) panel12Mode29MatVecRange64) panel12Mode29MatVecRange96) panel12Mode29MatVecRange128) row

theorem panel12Mode30MatVec_eq :
    P2RoundedFactorCheckpointData.panel12MomentData.matvecs
        .even ⟨15, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel12MomentData.moments
        (P2RoundedFactorCheckpointData.panel12FlatCache.component
          .even ⟨15, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel12Mode30MatVecRange0) panel12Mode30MatVecRange32) panel12Mode30MatVecRange64) panel12Mode30MatVecRange96) panel12Mode30MatVecRange128) row

theorem panel12Mode31MatVec_eq :
    P2RoundedFactorCheckpointData.panel12MomentData.matvecs
        .odd ⟨15, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel12MomentData.moments
        (P2RoundedFactorCheckpointData.panel12FlatCache.component
          .odd ⟨15, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel12Mode31MatVecRange0) panel12Mode31MatVecRange32) panel12Mode31MatVecRange64) panel12Mode31MatVecRange96) panel12Mode31MatVecRange128) row

theorem panel12Mode32MatVec_eq :
    P2RoundedFactorCheckpointData.panel12MomentData.matvecs
        .even ⟨16, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel12MomentData.moments
        (P2RoundedFactorCheckpointData.panel12FlatCache.component
          .even ⟨16, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel12Mode32MatVecRange0) panel12Mode32MatVecRange32) panel12Mode32MatVecRange64) panel12Mode32MatVecRange96) panel12Mode32MatVecRange128) row

theorem panel12Mode33MatVec_eq :
    P2RoundedFactorCheckpointData.panel12MomentData.matvecs
        .odd ⟨16, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel12MomentData.moments
        (P2RoundedFactorCheckpointData.panel12FlatCache.component
          .odd ⟨16, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel12Mode33MatVecRange0) panel12Mode33MatVecRange32) panel12Mode33MatVecRange64) panel12Mode33MatVecRange96) panel12Mode33MatVecRange128) row

theorem panel12Mode34MatVec_eq :
    P2RoundedFactorCheckpointData.panel12MomentData.matvecs
        .even ⟨17, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel12MomentData.moments
        (P2RoundedFactorCheckpointData.panel12FlatCache.component
          .even ⟨17, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel12Mode34MatVecRange0) panel12Mode34MatVecRange32) panel12Mode34MatVecRange64) panel12Mode34MatVecRange96) panel12Mode34MatVecRange128) row

theorem panel12Mode35MatVec_eq :
    P2RoundedFactorCheckpointData.panel12MomentData.matvecs
        .odd ⟨17, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel12MomentData.moments
        (P2RoundedFactorCheckpointData.panel12FlatCache.component
          .odd ⟨17, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel12Mode35MatVecRange0) panel12Mode35MatVecRange32) panel12Mode35MatVecRange64) panel12Mode35MatVecRange96) panel12Mode35MatVecRange128) row

theorem panel12Mode36MatVec_eq :
    P2RoundedFactorCheckpointData.panel12MomentData.matvecs
        .even ⟨18, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel12MomentData.moments
        (P2RoundedFactorCheckpointData.panel12FlatCache.component
          .even ⟨18, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel12Mode36MatVecRange0) panel12Mode36MatVecRange32) panel12Mode36MatVecRange64) panel12Mode36MatVecRange96) panel12Mode36MatVecRange128) row

theorem panel12Mode37MatVec_eq :
    P2RoundedFactorCheckpointData.panel12MomentData.matvecs
        .odd ⟨18, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel12MomentData.moments
        (P2RoundedFactorCheckpointData.panel12FlatCache.component
          .odd ⟨18, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel12Mode37MatVecRange0) panel12Mode37MatVecRange32) panel12Mode37MatVecRange64) panel12Mode37MatVecRange96) panel12Mode37MatVecRange128) row

theorem panel12Mode38MatVec_eq :
    P2RoundedFactorCheckpointData.panel12MomentData.matvecs
        .even ⟨19, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel12MomentData.moments
        (P2RoundedFactorCheckpointData.panel12FlatCache.component
          .even ⟨19, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel12Mode38MatVecRange0) panel12Mode38MatVecRange32) panel12Mode38MatVecRange64) panel12Mode38MatVecRange96) panel12Mode38MatVecRange128) row

theorem panel12Mode39MatVec_eq :
    P2RoundedFactorCheckpointData.panel12MomentData.matvecs
        .odd ⟨19, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel12MomentData.moments
        (P2RoundedFactorCheckpointData.panel12FlatCache.component
          .odd ⟨19, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel12Mode39MatVecRange0) panel12Mode39MatVecRange32) panel12Mode39MatVecRange64) panel12Mode39MatVecRange96) panel12Mode39MatVecRange128) row

theorem panel12Mode40MatVec_eq :
    P2RoundedFactorCheckpointData.panel12MomentData.matvecs
        .even ⟨20, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel12MomentData.moments
        (P2RoundedFactorCheckpointData.panel12FlatCache.component
          .even ⟨20, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel12Mode40MatVecRange0) panel12Mode40MatVecRange32) panel12Mode40MatVecRange64) panel12Mode40MatVecRange96) panel12Mode40MatVecRange128) row

theorem panel12Mode41MatVec_eq :
    P2RoundedFactorCheckpointData.panel12MomentData.matvecs
        .odd ⟨20, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel12MomentData.moments
        (P2RoundedFactorCheckpointData.panel12FlatCache.component
          .odd ⟨20, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel12Mode41MatVecRange0) panel12Mode41MatVecRange32) panel12Mode41MatVecRange64) panel12Mode41MatVecRange96) panel12Mode41MatVecRange128) row

theorem panel12Mode42MatVec_eq :
    P2RoundedFactorCheckpointData.panel12MomentData.matvecs
        .even ⟨21, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel12MomentData.moments
        (P2RoundedFactorCheckpointData.panel12FlatCache.component
          .even ⟨21, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel12Mode42MatVecRange0) panel12Mode42MatVecRange32) panel12Mode42MatVecRange64) panel12Mode42MatVecRange96) panel12Mode42MatVecRange128) row

theorem panel12Mode43MatVec_eq :
    P2RoundedFactorCheckpointData.panel12MomentData.matvecs
        .odd ⟨21, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel12MomentData.moments
        (P2RoundedFactorCheckpointData.panel12FlatCache.component
          .odd ⟨21, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel12Mode43MatVecRange0) panel12Mode43MatVecRange32) panel12Mode43MatVecRange64) panel12Mode43MatVecRange96) panel12Mode43MatVecRange128) row

theorem panel12Mode44MatVec_eq :
    P2RoundedFactorCheckpointData.panel12MomentData.matvecs
        .even ⟨22, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel12MomentData.moments
        (P2RoundedFactorCheckpointData.panel12FlatCache.component
          .even ⟨22, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel12Mode44MatVecRange0) panel12Mode44MatVecRange32) panel12Mode44MatVecRange64) panel12Mode44MatVecRange96) panel12Mode44MatVecRange128) row

theorem panel12Mode45MatVec_eq :
    P2RoundedFactorCheckpointData.panel12MomentData.matvecs
        .odd ⟨22, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel12MomentData.moments
        (P2RoundedFactorCheckpointData.panel12FlatCache.component
          .odd ⟨22, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel12Mode45MatVecRange0) panel12Mode45MatVecRange32) panel12Mode45MatVecRange64) panel12Mode45MatVecRange96) panel12Mode45MatVecRange128) row

theorem panel12Mode46MatVec_eq :
    P2RoundedFactorCheckpointData.panel12MomentData.matvecs
        .even ⟨23, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel12MomentData.moments
        (P2RoundedFactorCheckpointData.panel12FlatCache.component
          .even ⟨23, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel12Mode46MatVecRange0) panel12Mode46MatVecRange32) panel12Mode46MatVecRange64) panel12Mode46MatVecRange96) panel12Mode46MatVecRange128) row

theorem panel12Mode47MatVec_eq :
    P2RoundedFactorCheckpointData.panel12MomentData.matvecs
        .odd ⟨23, by decide⟩ =
      P2RoundedTripleMoment.hankelMatVecFromMoments
        P2RoundedFactorCheckpointData.panel12MomentData.moments
        (P2RoundedFactorCheckpointData.panel12FlatCache.component
          .odd ⟨23, by decide⟩).coeffs := by
  apply vector_ext_fin
  intro row
  exact P2RoundedGeneratedCertificate.FinRangeAll.to_forall
    (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (P2RoundedGeneratedCertificate.FinRangeAll.combine
        (panel12Mode47MatVecRange0) panel12Mode47MatVecRange32) panel12Mode47MatVecRange64) panel12Mode47MatVecRange96) panel12Mode47MatVecRange128) row

theorem panel12MomentData_correct :
    P2RoundedFactorCheckpointData.panel12MomentData.CorrectFor
      P2RoundedFactorCheckpointData.panel12FlatCache := by
  apply PanelMomentData.CorrectFor.of_vector_eq
      panel12DefectMoments_eq panel12ComponentLengthLe
  intro kind i
  cases kind with
  | even =>
      fin_cases i
      · exact panel12Mode0MatVec_eq
      · exact panel12Mode2MatVec_eq
      · exact panel12Mode4MatVec_eq
      · exact panel12Mode6MatVec_eq
      · exact panel12Mode8MatVec_eq
      · exact panel12Mode10MatVec_eq
      · exact panel12Mode12MatVec_eq
      · exact panel12Mode14MatVec_eq
      · exact panel12Mode16MatVec_eq
      · exact panel12Mode18MatVec_eq
      · exact panel12Mode20MatVec_eq
      · exact panel12Mode22MatVec_eq
      · exact panel12Mode24MatVec_eq
      · exact panel12Mode26MatVec_eq
      · exact panel12Mode28MatVec_eq
      · exact panel12Mode30MatVec_eq
      · exact panel12Mode32MatVec_eq
      · exact panel12Mode34MatVec_eq
      · exact panel12Mode36MatVec_eq
      · exact panel12Mode38MatVec_eq
      · exact panel12Mode40MatVec_eq
      · exact panel12Mode42MatVec_eq
      · exact panel12Mode44MatVec_eq
      · exact panel12Mode46MatVec_eq
  | odd =>
      fin_cases i
      · exact panel12Mode1MatVec_eq
      · exact panel12Mode3MatVec_eq
      · exact panel12Mode5MatVec_eq
      · exact panel12Mode7MatVec_eq
      · exact panel12Mode9MatVec_eq
      · exact panel12Mode11MatVec_eq
      · exact panel12Mode13MatVec_eq
      · exact panel12Mode15MatVec_eq
      · exact panel12Mode17MatVec_eq
      · exact panel12Mode19MatVec_eq
      · exact panel12Mode21MatVec_eq
      · exact panel12Mode23MatVec_eq
      · exact panel12Mode25MatVec_eq
      · exact panel12Mode27MatVec_eq
      · exact panel12Mode29MatVec_eq
      · exact panel12Mode31MatVec_eq
      · exact panel12Mode33MatVec_eq
      · exact panel12Mode35MatVec_eq
      · exact panel12Mode37MatVec_eq
      · exact panel12Mode39MatVec_eq
      · exact panel12Mode41MatVec_eq
      · exact panel12Mode43MatVec_eq
      · exact panel12Mode45MatVec_eq
      · exact panel12Mode47MatVec_eq

end RHP2Bridge
