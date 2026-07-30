import RHBridge.P2RoundedFactorCheckpointData23

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel23FactorChunk10 :
    P2RoundedFactorCheckpointData.panel23Prefix40 =
      normalizedPrefixTermAtomApprox ⟨40, by decide⟩ ⟨23, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel23Prefix41 =
      normalizedPrefixTermAtomApprox ⟨41, by decide⟩ ⟨23, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel23Prefix42 =
      normalizedPrefixTermAtomApprox ⟨42, by decide⟩ ⟨23, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel23Prefix43 =
      normalizedPrefixTermAtomApprox ⟨43, by decide⟩ ⟨23, by decide⟩ := by
  decide +kernel

theorem panel23Prefix40_eq :
    P2RoundedFactorCheckpointData.panel23Prefix40 =
      normalizedPrefixTermAtomApprox ⟨40, by decide⟩ ⟨23, by decide⟩ := by
  exact panel23FactorChunk10.1

theorem panel23Prefix41_eq :
    P2RoundedFactorCheckpointData.panel23Prefix41 =
      normalizedPrefixTermAtomApprox ⟨41, by decide⟩ ⟨23, by decide⟩ := by
  exact panel23FactorChunk10.2.1

theorem panel23Prefix42_eq :
    P2RoundedFactorCheckpointData.panel23Prefix42 =
      normalizedPrefixTermAtomApprox ⟨42, by decide⟩ ⟨23, by decide⟩ := by
  exact panel23FactorChunk10.2.2.1

theorem panel23Prefix43_eq :
    P2RoundedFactorCheckpointData.panel23Prefix43 =
      normalizedPrefixTermAtomApprox ⟨43, by decide⟩ ⟨23, by decide⟩ := by
  exact panel23FactorChunk10.2.2.2

end RHP2Bridge
