import RHBridge.P2RoundedFactorCheckpointData2

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel2FactorChunk10 :
    P2RoundedFactorCheckpointData.panel2Prefix40 =
      normalizedPrefixTermAtomApprox ⟨40, by decide⟩ ⟨2, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel2Prefix41 =
      normalizedPrefixTermAtomApprox ⟨41, by decide⟩ ⟨2, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel2Prefix42 =
      normalizedPrefixTermAtomApprox ⟨42, by decide⟩ ⟨2, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel2Prefix43 =
      normalizedPrefixTermAtomApprox ⟨43, by decide⟩ ⟨2, by decide⟩ := by
  decide +kernel

theorem panel2Prefix40_eq :
    P2RoundedFactorCheckpointData.panel2Prefix40 =
      normalizedPrefixTermAtomApprox ⟨40, by decide⟩ ⟨2, by decide⟩ := by
  exact panel2FactorChunk10.1

theorem panel2Prefix41_eq :
    P2RoundedFactorCheckpointData.panel2Prefix41 =
      normalizedPrefixTermAtomApprox ⟨41, by decide⟩ ⟨2, by decide⟩ := by
  exact panel2FactorChunk10.2.1

theorem panel2Prefix42_eq :
    P2RoundedFactorCheckpointData.panel2Prefix42 =
      normalizedPrefixTermAtomApprox ⟨42, by decide⟩ ⟨2, by decide⟩ := by
  exact panel2FactorChunk10.2.2.1

theorem panel2Prefix43_eq :
    P2RoundedFactorCheckpointData.panel2Prefix43 =
      normalizedPrefixTermAtomApprox ⟨43, by decide⟩ ⟨2, by decide⟩ := by
  exact panel2FactorChunk10.2.2.2

end RHP2Bridge
