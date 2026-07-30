import RHBridge.P2RoundedFactorCheckpointData13

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel13FactorChunk10 :
    P2RoundedFactorCheckpointData.panel13Prefix40 =
      normalizedPrefixTermAtomApprox ⟨40, by decide⟩ ⟨13, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel13Prefix41 =
      normalizedPrefixTermAtomApprox ⟨41, by decide⟩ ⟨13, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel13Prefix42 =
      normalizedPrefixTermAtomApprox ⟨42, by decide⟩ ⟨13, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel13Prefix43 =
      normalizedPrefixTermAtomApprox ⟨43, by decide⟩ ⟨13, by decide⟩ := by
  decide +kernel

theorem panel13Prefix40_eq :
    P2RoundedFactorCheckpointData.panel13Prefix40 =
      normalizedPrefixTermAtomApprox ⟨40, by decide⟩ ⟨13, by decide⟩ := by
  exact panel13FactorChunk10.1

theorem panel13Prefix41_eq :
    P2RoundedFactorCheckpointData.panel13Prefix41 =
      normalizedPrefixTermAtomApprox ⟨41, by decide⟩ ⟨13, by decide⟩ := by
  exact panel13FactorChunk10.2.1

theorem panel13Prefix42_eq :
    P2RoundedFactorCheckpointData.panel13Prefix42 =
      normalizedPrefixTermAtomApprox ⟨42, by decide⟩ ⟨13, by decide⟩ := by
  exact panel13FactorChunk10.2.2.1

theorem panel13Prefix43_eq :
    P2RoundedFactorCheckpointData.panel13Prefix43 =
      normalizedPrefixTermAtomApprox ⟨43, by decide⟩ ⟨13, by decide⟩ := by
  exact panel13FactorChunk10.2.2.2

end RHP2Bridge
