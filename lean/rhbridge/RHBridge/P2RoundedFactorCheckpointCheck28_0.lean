import RHBridge.P2RoundedFactorCheckpointData28

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel28FactorChunk0 :
    P2RoundedFactorCheckpointData.panel28Prefix0 =
      normalizedPrefixTermAtomApprox ⟨0, by decide⟩ ⟨28, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel28Prefix1 =
      normalizedPrefixTermAtomApprox ⟨1, by decide⟩ ⟨28, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel28Prefix2 =
      normalizedPrefixTermAtomApprox ⟨2, by decide⟩ ⟨28, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel28Prefix3 =
      normalizedPrefixTermAtomApprox ⟨3, by decide⟩ ⟨28, by decide⟩ := by
  decide +kernel

theorem panel28Prefix0_eq :
    P2RoundedFactorCheckpointData.panel28Prefix0 =
      normalizedPrefixTermAtomApprox ⟨0, by decide⟩ ⟨28, by decide⟩ := by
  exact panel28FactorChunk0.1

theorem panel28Prefix1_eq :
    P2RoundedFactorCheckpointData.panel28Prefix1 =
      normalizedPrefixTermAtomApprox ⟨1, by decide⟩ ⟨28, by decide⟩ := by
  exact panel28FactorChunk0.2.1

theorem panel28Prefix2_eq :
    P2RoundedFactorCheckpointData.panel28Prefix2 =
      normalizedPrefixTermAtomApprox ⟨2, by decide⟩ ⟨28, by decide⟩ := by
  exact panel28FactorChunk0.2.2.1

theorem panel28Prefix3_eq :
    P2RoundedFactorCheckpointData.panel28Prefix3 =
      normalizedPrefixTermAtomApprox ⟨3, by decide⟩ ⟨28, by decide⟩ := by
  exact panel28FactorChunk0.2.2.2

end RHP2Bridge
