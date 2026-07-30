import RHBridge.P2RoundedFactorCheckpointData22

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel22FactorChunk0 :
    P2RoundedFactorCheckpointData.panel22Prefix0 =
      normalizedPrefixTermAtomApprox ⟨0, by decide⟩ ⟨22, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel22Prefix1 =
      normalizedPrefixTermAtomApprox ⟨1, by decide⟩ ⟨22, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel22Prefix2 =
      normalizedPrefixTermAtomApprox ⟨2, by decide⟩ ⟨22, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel22Prefix3 =
      normalizedPrefixTermAtomApprox ⟨3, by decide⟩ ⟨22, by decide⟩ := by
  decide +kernel

theorem panel22Prefix0_eq :
    P2RoundedFactorCheckpointData.panel22Prefix0 =
      normalizedPrefixTermAtomApprox ⟨0, by decide⟩ ⟨22, by decide⟩ := by
  exact panel22FactorChunk0.1

theorem panel22Prefix1_eq :
    P2RoundedFactorCheckpointData.panel22Prefix1 =
      normalizedPrefixTermAtomApprox ⟨1, by decide⟩ ⟨22, by decide⟩ := by
  exact panel22FactorChunk0.2.1

theorem panel22Prefix2_eq :
    P2RoundedFactorCheckpointData.panel22Prefix2 =
      normalizedPrefixTermAtomApprox ⟨2, by decide⟩ ⟨22, by decide⟩ := by
  exact panel22FactorChunk0.2.2.1

theorem panel22Prefix3_eq :
    P2RoundedFactorCheckpointData.panel22Prefix3 =
      normalizedPrefixTermAtomApprox ⟨3, by decide⟩ ⟨22, by decide⟩ := by
  exact panel22FactorChunk0.2.2.2

end RHP2Bridge
