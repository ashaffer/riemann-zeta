import RHBridge.P2RoundedFactorCheckpointData16

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel16FactorChunk13 :
    P2RoundedFactorCheckpointData.panel16Prefix52 =
      normalizedPrefixTermAtomApprox ⟨52, by decide⟩ ⟨16, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel16Prefix53 =
      normalizedPrefixTermAtomApprox ⟨53, by decide⟩ ⟨16, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel16Prefix54 =
      normalizedPrefixTermAtomApprox ⟨54, by decide⟩ ⟨16, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel16Prefix55 =
      normalizedPrefixTermAtomApprox ⟨55, by decide⟩ ⟨16, by decide⟩ := by
  decide +kernel

theorem panel16Prefix52_eq :
    P2RoundedFactorCheckpointData.panel16Prefix52 =
      normalizedPrefixTermAtomApprox ⟨52, by decide⟩ ⟨16, by decide⟩ := by
  exact panel16FactorChunk13.1

theorem panel16Prefix53_eq :
    P2RoundedFactorCheckpointData.panel16Prefix53 =
      normalizedPrefixTermAtomApprox ⟨53, by decide⟩ ⟨16, by decide⟩ := by
  exact panel16FactorChunk13.2.1

theorem panel16Prefix54_eq :
    P2RoundedFactorCheckpointData.panel16Prefix54 =
      normalizedPrefixTermAtomApprox ⟨54, by decide⟩ ⟨16, by decide⟩ := by
  exact panel16FactorChunk13.2.2.1

theorem panel16Prefix55_eq :
    P2RoundedFactorCheckpointData.panel16Prefix55 =
      normalizedPrefixTermAtomApprox ⟨55, by decide⟩ ⟨16, by decide⟩ := by
  exact panel16FactorChunk13.2.2.2

end RHP2Bridge
