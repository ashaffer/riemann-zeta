import RHBridge.P2RoundedFactorCheckpointData15

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel15FactorChunk8 :
    P2RoundedFactorCheckpointData.panel15Prefix32 =
      normalizedPrefixTermAtomApprox ⟨32, by decide⟩ ⟨15, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel15Prefix33 =
      normalizedPrefixTermAtomApprox ⟨33, by decide⟩ ⟨15, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel15Prefix34 =
      normalizedPrefixTermAtomApprox ⟨34, by decide⟩ ⟨15, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel15Prefix35 =
      normalizedPrefixTermAtomApprox ⟨35, by decide⟩ ⟨15, by decide⟩ := by
  decide +kernel

theorem panel15Prefix32_eq :
    P2RoundedFactorCheckpointData.panel15Prefix32 =
      normalizedPrefixTermAtomApprox ⟨32, by decide⟩ ⟨15, by decide⟩ := by
  exact panel15FactorChunk8.1

theorem panel15Prefix33_eq :
    P2RoundedFactorCheckpointData.panel15Prefix33 =
      normalizedPrefixTermAtomApprox ⟨33, by decide⟩ ⟨15, by decide⟩ := by
  exact panel15FactorChunk8.2.1

theorem panel15Prefix34_eq :
    P2RoundedFactorCheckpointData.panel15Prefix34 =
      normalizedPrefixTermAtomApprox ⟨34, by decide⟩ ⟨15, by decide⟩ := by
  exact panel15FactorChunk8.2.2.1

theorem panel15Prefix35_eq :
    P2RoundedFactorCheckpointData.panel15Prefix35 =
      normalizedPrefixTermAtomApprox ⟨35, by decide⟩ ⟨15, by decide⟩ := by
  exact panel15FactorChunk8.2.2.2

end RHP2Bridge
