import RHBridge.P2RoundedFactorCheckpointData21

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel21FactorChunk8 :
    P2RoundedFactorCheckpointData.panel21Prefix32 =
      normalizedPrefixTermAtomApprox ⟨32, by decide⟩ ⟨21, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel21Prefix33 =
      normalizedPrefixTermAtomApprox ⟨33, by decide⟩ ⟨21, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel21Prefix34 =
      normalizedPrefixTermAtomApprox ⟨34, by decide⟩ ⟨21, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel21Prefix35 =
      normalizedPrefixTermAtomApprox ⟨35, by decide⟩ ⟨21, by decide⟩ := by
  decide +kernel

theorem panel21Prefix32_eq :
    P2RoundedFactorCheckpointData.panel21Prefix32 =
      normalizedPrefixTermAtomApprox ⟨32, by decide⟩ ⟨21, by decide⟩ := by
  exact panel21FactorChunk8.1

theorem panel21Prefix33_eq :
    P2RoundedFactorCheckpointData.panel21Prefix33 =
      normalizedPrefixTermAtomApprox ⟨33, by decide⟩ ⟨21, by decide⟩ := by
  exact panel21FactorChunk8.2.1

theorem panel21Prefix34_eq :
    P2RoundedFactorCheckpointData.panel21Prefix34 =
      normalizedPrefixTermAtomApprox ⟨34, by decide⟩ ⟨21, by decide⟩ := by
  exact panel21FactorChunk8.2.2.1

theorem panel21Prefix35_eq :
    P2RoundedFactorCheckpointData.panel21Prefix35 =
      normalizedPrefixTermAtomApprox ⟨35, by decide⟩ ⟨21, by decide⟩ := by
  exact panel21FactorChunk8.2.2.2

end RHP2Bridge
