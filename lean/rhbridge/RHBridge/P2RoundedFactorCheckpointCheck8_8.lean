import RHBridge.P2RoundedFactorCheckpointData8

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel8FactorChunk8 :
    P2RoundedFactorCheckpointData.panel8Prefix32 =
      normalizedPrefixTermAtomApprox ⟨32, by decide⟩ ⟨8, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel8Prefix33 =
      normalizedPrefixTermAtomApprox ⟨33, by decide⟩ ⟨8, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel8Prefix34 =
      normalizedPrefixTermAtomApprox ⟨34, by decide⟩ ⟨8, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel8Prefix35 =
      normalizedPrefixTermAtomApprox ⟨35, by decide⟩ ⟨8, by decide⟩ := by
  decide +kernel

theorem panel8Prefix32_eq :
    P2RoundedFactorCheckpointData.panel8Prefix32 =
      normalizedPrefixTermAtomApprox ⟨32, by decide⟩ ⟨8, by decide⟩ := by
  exact panel8FactorChunk8.1

theorem panel8Prefix33_eq :
    P2RoundedFactorCheckpointData.panel8Prefix33 =
      normalizedPrefixTermAtomApprox ⟨33, by decide⟩ ⟨8, by decide⟩ := by
  exact panel8FactorChunk8.2.1

theorem panel8Prefix34_eq :
    P2RoundedFactorCheckpointData.panel8Prefix34 =
      normalizedPrefixTermAtomApprox ⟨34, by decide⟩ ⟨8, by decide⟩ := by
  exact panel8FactorChunk8.2.2.1

theorem panel8Prefix35_eq :
    P2RoundedFactorCheckpointData.panel8Prefix35 =
      normalizedPrefixTermAtomApprox ⟨35, by decide⟩ ⟨8, by decide⟩ := by
  exact panel8FactorChunk8.2.2.2

end RHP2Bridge
