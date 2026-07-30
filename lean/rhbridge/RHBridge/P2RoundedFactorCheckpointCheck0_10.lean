import RHBridge.P2RoundedFactorCheckpointData0

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel0FactorChunk10 :
    P2RoundedFactorCheckpointData.panel0Prefix40 =
      normalizedPrefixTermAtomApprox ⟨40, by decide⟩ ⟨0, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel0Prefix41 =
      normalizedPrefixTermAtomApprox ⟨41, by decide⟩ ⟨0, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel0Prefix42 =
      normalizedPrefixTermAtomApprox ⟨42, by decide⟩ ⟨0, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel0Prefix43 =
      normalizedPrefixTermAtomApprox ⟨43, by decide⟩ ⟨0, by decide⟩ := by
  decide +kernel

theorem panel0Prefix40_eq :
    P2RoundedFactorCheckpointData.panel0Prefix40 =
      normalizedPrefixTermAtomApprox ⟨40, by decide⟩ ⟨0, by decide⟩ := by
  exact panel0FactorChunk10.1

theorem panel0Prefix41_eq :
    P2RoundedFactorCheckpointData.panel0Prefix41 =
      normalizedPrefixTermAtomApprox ⟨41, by decide⟩ ⟨0, by decide⟩ := by
  exact panel0FactorChunk10.2.1

theorem panel0Prefix42_eq :
    P2RoundedFactorCheckpointData.panel0Prefix42 =
      normalizedPrefixTermAtomApprox ⟨42, by decide⟩ ⟨0, by decide⟩ := by
  exact panel0FactorChunk10.2.2.1

theorem panel0Prefix43_eq :
    P2RoundedFactorCheckpointData.panel0Prefix43 =
      normalizedPrefixTermAtomApprox ⟨43, by decide⟩ ⟨0, by decide⟩ := by
  exact panel0FactorChunk10.2.2.2

end RHP2Bridge
