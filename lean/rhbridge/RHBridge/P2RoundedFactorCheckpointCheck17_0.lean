import RHBridge.P2RoundedFactorCheckpointData17

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel17FactorChunk0 :
    P2RoundedFactorCheckpointData.panel17Prefix0 =
      normalizedPrefixTermAtomApprox ⟨0, by decide⟩ ⟨17, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel17Prefix1 =
      normalizedPrefixTermAtomApprox ⟨1, by decide⟩ ⟨17, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel17Prefix2 =
      normalizedPrefixTermAtomApprox ⟨2, by decide⟩ ⟨17, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel17Prefix3 =
      normalizedPrefixTermAtomApprox ⟨3, by decide⟩ ⟨17, by decide⟩ := by
  decide +kernel

theorem panel17Prefix0_eq :
    P2RoundedFactorCheckpointData.panel17Prefix0 =
      normalizedPrefixTermAtomApprox ⟨0, by decide⟩ ⟨17, by decide⟩ := by
  exact panel17FactorChunk0.1

theorem panel17Prefix1_eq :
    P2RoundedFactorCheckpointData.panel17Prefix1 =
      normalizedPrefixTermAtomApprox ⟨1, by decide⟩ ⟨17, by decide⟩ := by
  exact panel17FactorChunk0.2.1

theorem panel17Prefix2_eq :
    P2RoundedFactorCheckpointData.panel17Prefix2 =
      normalizedPrefixTermAtomApprox ⟨2, by decide⟩ ⟨17, by decide⟩ := by
  exact panel17FactorChunk0.2.2.1

theorem panel17Prefix3_eq :
    P2RoundedFactorCheckpointData.panel17Prefix3 =
      normalizedPrefixTermAtomApprox ⟨3, by decide⟩ ⟨17, by decide⟩ := by
  exact panel17FactorChunk0.2.2.2

end RHP2Bridge
