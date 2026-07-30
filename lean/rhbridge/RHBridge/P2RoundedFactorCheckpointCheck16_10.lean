import RHBridge.P2RoundedFactorCheckpointData16

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel16FactorChunk10 :
    P2RoundedFactorCheckpointData.panel16Prefix40 =
      normalizedPrefixTermAtomApprox ⟨40, by decide⟩ ⟨16, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel16Prefix41 =
      normalizedPrefixTermAtomApprox ⟨41, by decide⟩ ⟨16, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel16Prefix42 =
      normalizedPrefixTermAtomApprox ⟨42, by decide⟩ ⟨16, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel16Prefix43 =
      normalizedPrefixTermAtomApprox ⟨43, by decide⟩ ⟨16, by decide⟩ := by
  decide +kernel

theorem panel16Prefix40_eq :
    P2RoundedFactorCheckpointData.panel16Prefix40 =
      normalizedPrefixTermAtomApprox ⟨40, by decide⟩ ⟨16, by decide⟩ := by
  exact panel16FactorChunk10.1

theorem panel16Prefix41_eq :
    P2RoundedFactorCheckpointData.panel16Prefix41 =
      normalizedPrefixTermAtomApprox ⟨41, by decide⟩ ⟨16, by decide⟩ := by
  exact panel16FactorChunk10.2.1

theorem panel16Prefix42_eq :
    P2RoundedFactorCheckpointData.panel16Prefix42 =
      normalizedPrefixTermAtomApprox ⟨42, by decide⟩ ⟨16, by decide⟩ := by
  exact panel16FactorChunk10.2.2.1

theorem panel16Prefix43_eq :
    P2RoundedFactorCheckpointData.panel16Prefix43 =
      normalizedPrefixTermAtomApprox ⟨43, by decide⟩ ⟨16, by decide⟩ := by
  exact panel16FactorChunk10.2.2.2

end RHP2Bridge
