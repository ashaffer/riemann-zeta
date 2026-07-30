import RHBridge.P2RoundedFactorCheckpointData8

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel8FactorChunk5 :
    P2RoundedFactorCheckpointData.panel8Prefix20 =
      normalizedPrefixTermAtomApprox ⟨20, by decide⟩ ⟨8, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel8Prefix21 =
      normalizedPrefixTermAtomApprox ⟨21, by decide⟩ ⟨8, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel8Prefix22 =
      normalizedPrefixTermAtomApprox ⟨22, by decide⟩ ⟨8, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel8Prefix23 =
      normalizedPrefixTermAtomApprox ⟨23, by decide⟩ ⟨8, by decide⟩ := by
  decide +kernel

theorem panel8Prefix20_eq :
    P2RoundedFactorCheckpointData.panel8Prefix20 =
      normalizedPrefixTermAtomApprox ⟨20, by decide⟩ ⟨8, by decide⟩ := by
  exact panel8FactorChunk5.1

theorem panel8Prefix21_eq :
    P2RoundedFactorCheckpointData.panel8Prefix21 =
      normalizedPrefixTermAtomApprox ⟨21, by decide⟩ ⟨8, by decide⟩ := by
  exact panel8FactorChunk5.2.1

theorem panel8Prefix22_eq :
    P2RoundedFactorCheckpointData.panel8Prefix22 =
      normalizedPrefixTermAtomApprox ⟨22, by decide⟩ ⟨8, by decide⟩ := by
  exact panel8FactorChunk5.2.2.1

theorem panel8Prefix23_eq :
    P2RoundedFactorCheckpointData.panel8Prefix23 =
      normalizedPrefixTermAtomApprox ⟨23, by decide⟩ ⟨8, by decide⟩ := by
  exact panel8FactorChunk5.2.2.2

end RHP2Bridge
