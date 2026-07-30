import RHBridge.P2RoundedFactorCheckpointData8

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel8FactorChunk12 :
    P2RoundedFactorCheckpointData.panel8Prefix48 =
      normalizedPrefixTermAtomApprox ⟨48, by decide⟩ ⟨8, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel8Prefix49 =
      normalizedPrefixTermAtomApprox ⟨49, by decide⟩ ⟨8, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel8Prefix50 =
      normalizedPrefixTermAtomApprox ⟨50, by decide⟩ ⟨8, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel8Prefix51 =
      normalizedPrefixTermAtomApprox ⟨51, by decide⟩ ⟨8, by decide⟩ := by
  decide +kernel

theorem panel8Prefix48_eq :
    P2RoundedFactorCheckpointData.panel8Prefix48 =
      normalizedPrefixTermAtomApprox ⟨48, by decide⟩ ⟨8, by decide⟩ := by
  exact panel8FactorChunk12.1

theorem panel8Prefix49_eq :
    P2RoundedFactorCheckpointData.panel8Prefix49 =
      normalizedPrefixTermAtomApprox ⟨49, by decide⟩ ⟨8, by decide⟩ := by
  exact panel8FactorChunk12.2.1

theorem panel8Prefix50_eq :
    P2RoundedFactorCheckpointData.panel8Prefix50 =
      normalizedPrefixTermAtomApprox ⟨50, by decide⟩ ⟨8, by decide⟩ := by
  exact panel8FactorChunk12.2.2.1

theorem panel8Prefix51_eq :
    P2RoundedFactorCheckpointData.panel8Prefix51 =
      normalizedPrefixTermAtomApprox ⟨51, by decide⟩ ⟨8, by decide⟩ := by
  exact panel8FactorChunk12.2.2.2

end RHP2Bridge
