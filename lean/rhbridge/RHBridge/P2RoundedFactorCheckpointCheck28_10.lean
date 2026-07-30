import RHBridge.P2RoundedFactorCheckpointData28

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel28FactorChunk10 :
    P2RoundedFactorCheckpointData.panel28Prefix40 =
      normalizedPrefixTermAtomApprox ⟨40, by decide⟩ ⟨28, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel28Prefix41 =
      normalizedPrefixTermAtomApprox ⟨41, by decide⟩ ⟨28, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel28Prefix42 =
      normalizedPrefixTermAtomApprox ⟨42, by decide⟩ ⟨28, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel28Prefix43 =
      normalizedPrefixTermAtomApprox ⟨43, by decide⟩ ⟨28, by decide⟩ := by
  decide +kernel

theorem panel28Prefix40_eq :
    P2RoundedFactorCheckpointData.panel28Prefix40 =
      normalizedPrefixTermAtomApprox ⟨40, by decide⟩ ⟨28, by decide⟩ := by
  exact panel28FactorChunk10.1

theorem panel28Prefix41_eq :
    P2RoundedFactorCheckpointData.panel28Prefix41 =
      normalizedPrefixTermAtomApprox ⟨41, by decide⟩ ⟨28, by decide⟩ := by
  exact panel28FactorChunk10.2.1

theorem panel28Prefix42_eq :
    P2RoundedFactorCheckpointData.panel28Prefix42 =
      normalizedPrefixTermAtomApprox ⟨42, by decide⟩ ⟨28, by decide⟩ := by
  exact panel28FactorChunk10.2.2.1

theorem panel28Prefix43_eq :
    P2RoundedFactorCheckpointData.panel28Prefix43 =
      normalizedPrefixTermAtomApprox ⟨43, by decide⟩ ⟨28, by decide⟩ := by
  exact panel28FactorChunk10.2.2.2

end RHP2Bridge
