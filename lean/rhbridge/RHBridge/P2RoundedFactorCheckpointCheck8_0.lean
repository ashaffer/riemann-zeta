import RHBridge.P2RoundedFactorCheckpointData8

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel8FactorChunk0 :
    P2RoundedFactorCheckpointData.panel8Prefix0 =
      normalizedPrefixTermAtomApprox ⟨0, by decide⟩ ⟨8, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel8Prefix1 =
      normalizedPrefixTermAtomApprox ⟨1, by decide⟩ ⟨8, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel8Prefix2 =
      normalizedPrefixTermAtomApprox ⟨2, by decide⟩ ⟨8, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel8Prefix3 =
      normalizedPrefixTermAtomApprox ⟨3, by decide⟩ ⟨8, by decide⟩ := by
  decide +kernel

theorem panel8Prefix0_eq :
    P2RoundedFactorCheckpointData.panel8Prefix0 =
      normalizedPrefixTermAtomApprox ⟨0, by decide⟩ ⟨8, by decide⟩ := by
  exact panel8FactorChunk0.1

theorem panel8Prefix1_eq :
    P2RoundedFactorCheckpointData.panel8Prefix1 =
      normalizedPrefixTermAtomApprox ⟨1, by decide⟩ ⟨8, by decide⟩ := by
  exact panel8FactorChunk0.2.1

theorem panel8Prefix2_eq :
    P2RoundedFactorCheckpointData.panel8Prefix2 =
      normalizedPrefixTermAtomApprox ⟨2, by decide⟩ ⟨8, by decide⟩ := by
  exact panel8FactorChunk0.2.2.1

theorem panel8Prefix3_eq :
    P2RoundedFactorCheckpointData.panel8Prefix3 =
      normalizedPrefixTermAtomApprox ⟨3, by decide⟩ ⟨8, by decide⟩ := by
  exact panel8FactorChunk0.2.2.2

end RHP2Bridge
