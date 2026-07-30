import RHBridge.P2RoundedFactorCheckpointData4

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel4FactorChunk10 :
    P2RoundedFactorCheckpointData.panel4Prefix40 =
      normalizedPrefixTermAtomApprox ⟨40, by decide⟩ ⟨4, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel4Prefix41 =
      normalizedPrefixTermAtomApprox ⟨41, by decide⟩ ⟨4, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel4Prefix42 =
      normalizedPrefixTermAtomApprox ⟨42, by decide⟩ ⟨4, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel4Prefix43 =
      normalizedPrefixTermAtomApprox ⟨43, by decide⟩ ⟨4, by decide⟩ := by
  decide +kernel

theorem panel4Prefix40_eq :
    P2RoundedFactorCheckpointData.panel4Prefix40 =
      normalizedPrefixTermAtomApprox ⟨40, by decide⟩ ⟨4, by decide⟩ := by
  exact panel4FactorChunk10.1

theorem panel4Prefix41_eq :
    P2RoundedFactorCheckpointData.panel4Prefix41 =
      normalizedPrefixTermAtomApprox ⟨41, by decide⟩ ⟨4, by decide⟩ := by
  exact panel4FactorChunk10.2.1

theorem panel4Prefix42_eq :
    P2RoundedFactorCheckpointData.panel4Prefix42 =
      normalizedPrefixTermAtomApprox ⟨42, by decide⟩ ⟨4, by decide⟩ := by
  exact panel4FactorChunk10.2.2.1

theorem panel4Prefix43_eq :
    P2RoundedFactorCheckpointData.panel4Prefix43 =
      normalizedPrefixTermAtomApprox ⟨43, by decide⟩ ⟨4, by decide⟩ := by
  exact panel4FactorChunk10.2.2.2

end RHP2Bridge
