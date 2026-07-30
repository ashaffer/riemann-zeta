import RHBridge.P2RoundedFactorCheckpointData30

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel30FactorChunk5 :
    P2RoundedFactorCheckpointData.panel30Prefix20 =
      normalizedPrefixTermAtomApprox ⟨20, by decide⟩ ⟨30, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel30Prefix21 =
      normalizedPrefixTermAtomApprox ⟨21, by decide⟩ ⟨30, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel30Prefix22 =
      normalizedPrefixTermAtomApprox ⟨22, by decide⟩ ⟨30, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel30Prefix23 =
      normalizedPrefixTermAtomApprox ⟨23, by decide⟩ ⟨30, by decide⟩ := by
  decide +kernel

theorem panel30Prefix20_eq :
    P2RoundedFactorCheckpointData.panel30Prefix20 =
      normalizedPrefixTermAtomApprox ⟨20, by decide⟩ ⟨30, by decide⟩ := by
  exact panel30FactorChunk5.1

theorem panel30Prefix21_eq :
    P2RoundedFactorCheckpointData.panel30Prefix21 =
      normalizedPrefixTermAtomApprox ⟨21, by decide⟩ ⟨30, by decide⟩ := by
  exact panel30FactorChunk5.2.1

theorem panel30Prefix22_eq :
    P2RoundedFactorCheckpointData.panel30Prefix22 =
      normalizedPrefixTermAtomApprox ⟨22, by decide⟩ ⟨30, by decide⟩ := by
  exact panel30FactorChunk5.2.2.1

theorem panel30Prefix23_eq :
    P2RoundedFactorCheckpointData.panel30Prefix23 =
      normalizedPrefixTermAtomApprox ⟨23, by decide⟩ ⟨30, by decide⟩ := by
  exact panel30FactorChunk5.2.2.2

end RHP2Bridge
