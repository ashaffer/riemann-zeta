import RHBridge.P2RoundedFactorCheckpointData31

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel31FactorChunk8 :
    P2RoundedFactorCheckpointData.panel31Prefix32 =
      normalizedPrefixTermAtomApprox ⟨32, by decide⟩ ⟨31, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel31Prefix33 =
      normalizedPrefixTermAtomApprox ⟨33, by decide⟩ ⟨31, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel31Prefix34 =
      normalizedPrefixTermAtomApprox ⟨34, by decide⟩ ⟨31, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel31Prefix35 =
      normalizedPrefixTermAtomApprox ⟨35, by decide⟩ ⟨31, by decide⟩ := by
  decide +kernel

theorem panel31Prefix32_eq :
    P2RoundedFactorCheckpointData.panel31Prefix32 =
      normalizedPrefixTermAtomApprox ⟨32, by decide⟩ ⟨31, by decide⟩ := by
  exact panel31FactorChunk8.1

theorem panel31Prefix33_eq :
    P2RoundedFactorCheckpointData.panel31Prefix33 =
      normalizedPrefixTermAtomApprox ⟨33, by decide⟩ ⟨31, by decide⟩ := by
  exact panel31FactorChunk8.2.1

theorem panel31Prefix34_eq :
    P2RoundedFactorCheckpointData.panel31Prefix34 =
      normalizedPrefixTermAtomApprox ⟨34, by decide⟩ ⟨31, by decide⟩ := by
  exact panel31FactorChunk8.2.2.1

theorem panel31Prefix35_eq :
    P2RoundedFactorCheckpointData.panel31Prefix35 =
      normalizedPrefixTermAtomApprox ⟨35, by decide⟩ ⟨31, by decide⟩ := by
  exact panel31FactorChunk8.2.2.2

end RHP2Bridge
