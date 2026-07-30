import RHBridge.P2RoundedFactorCheckpointData21

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel21FactorChunk10 :
    P2RoundedFactorCheckpointData.panel21Prefix40 =
      normalizedPrefixTermAtomApprox ⟨40, by decide⟩ ⟨21, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel21Prefix41 =
      normalizedPrefixTermAtomApprox ⟨41, by decide⟩ ⟨21, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel21Prefix42 =
      normalizedPrefixTermAtomApprox ⟨42, by decide⟩ ⟨21, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel21Prefix43 =
      normalizedPrefixTermAtomApprox ⟨43, by decide⟩ ⟨21, by decide⟩ := by
  decide +kernel

theorem panel21Prefix40_eq :
    P2RoundedFactorCheckpointData.panel21Prefix40 =
      normalizedPrefixTermAtomApprox ⟨40, by decide⟩ ⟨21, by decide⟩ := by
  exact panel21FactorChunk10.1

theorem panel21Prefix41_eq :
    P2RoundedFactorCheckpointData.panel21Prefix41 =
      normalizedPrefixTermAtomApprox ⟨41, by decide⟩ ⟨21, by decide⟩ := by
  exact panel21FactorChunk10.2.1

theorem panel21Prefix42_eq :
    P2RoundedFactorCheckpointData.panel21Prefix42 =
      normalizedPrefixTermAtomApprox ⟨42, by decide⟩ ⟨21, by decide⟩ := by
  exact panel21FactorChunk10.2.2.1

theorem panel21Prefix43_eq :
    P2RoundedFactorCheckpointData.panel21Prefix43 =
      normalizedPrefixTermAtomApprox ⟨43, by decide⟩ ⟨21, by decide⟩ := by
  exact panel21FactorChunk10.2.2.2

end RHP2Bridge
