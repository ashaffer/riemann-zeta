import RHBridge.P2RoundedFactorCheckpointData30

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel30FactorChunk0 :
    P2RoundedFactorCheckpointData.panel30Prefix0 =
      normalizedPrefixTermAtomApprox ⟨0, by decide⟩ ⟨30, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel30Prefix1 =
      normalizedPrefixTermAtomApprox ⟨1, by decide⟩ ⟨30, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel30Prefix2 =
      normalizedPrefixTermAtomApprox ⟨2, by decide⟩ ⟨30, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel30Prefix3 =
      normalizedPrefixTermAtomApprox ⟨3, by decide⟩ ⟨30, by decide⟩ := by
  decide +kernel

theorem panel30Prefix0_eq :
    P2RoundedFactorCheckpointData.panel30Prefix0 =
      normalizedPrefixTermAtomApprox ⟨0, by decide⟩ ⟨30, by decide⟩ := by
  exact panel30FactorChunk0.1

theorem panel30Prefix1_eq :
    P2RoundedFactorCheckpointData.panel30Prefix1 =
      normalizedPrefixTermAtomApprox ⟨1, by decide⟩ ⟨30, by decide⟩ := by
  exact panel30FactorChunk0.2.1

theorem panel30Prefix2_eq :
    P2RoundedFactorCheckpointData.panel30Prefix2 =
      normalizedPrefixTermAtomApprox ⟨2, by decide⟩ ⟨30, by decide⟩ := by
  exact panel30FactorChunk0.2.2.1

theorem panel30Prefix3_eq :
    P2RoundedFactorCheckpointData.panel30Prefix3 =
      normalizedPrefixTermAtomApprox ⟨3, by decide⟩ ⟨30, by decide⟩ := by
  exact panel30FactorChunk0.2.2.2

end RHP2Bridge
